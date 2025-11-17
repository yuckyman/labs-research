#!/usr/bin/env python3
"""
Main script to process publications: query APIs, download PDFs, convert to markdown,
and create publication files. This orchestrates all the other scripts.
"""

import os
import sys
import json
import time
import subprocess
import requests
import xml.etree.ElementTree as ET
import tempfile
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from urllib.parse import quote


def query_crossref(author_name: str, orcid: Optional[str] = None, days_back: int = 7) -> List[Dict]:
    """Query Crossref API for publications."""
    publications = []
    
    try:
        # Build query
        query_parts = [f"query.author={quote(author_name)}"]
        if orcid:
            query_parts.append(f"orcid={orcid}")
        
        # Date filter
        date_from = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
        query_parts.append(f"filter=from-pub-date:{date_from}")
        
        query_parts.append("rows=50")
        query_parts.append("mailto=github-actions@example.com")
        
        url = f"https://api.crossref.org/works?{'&'.join(query_parts)}"
        
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        items = data.get('message', {}).get('items', [])
        
        for item in items:
            pub = {
                'title': item.get('title', [''])[0] if item.get('title') else '',
                'doi': item.get('DOI', ''),
                'year': item.get('published', {}).get('date-parts', [[None]])[0][0] if item.get('published', {}).get('date-parts') else None,
                'journal': item.get('container-title', [''])[0] if item.get('container-title') else '',
                'authors': [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in item.get('author', [])],
                'abstract': item.get('abstract', ''),
                'url': f"https://doi.org/{item.get('DOI', '')}" if item.get('DOI') else '',
                'source': 'crossref',
            }
            
            # Extract abstract from different possible locations
            if not pub['abstract']:
                # Try alternative abstract locations
                abstract_parts = []
                for key in ['abstract', 'description']:
                    if key in item:
                        abstract_parts.append(str(item[key]))
                pub['abstract'] = ' '.join(abstract_parts)
            
            if pub['title']:
                publications.append(pub)
        
        # Rate limiting
        time.sleep(1)
        
    except Exception as e:
        print(f"  Crossref query error for {author_name}: {e}", file=sys.stderr)
    
    return publications


def query_arxiv(author_name: str, days_back: int = 7) -> List[Dict]:
    """Query arXiv API for preprints."""
    publications = []
    
    try:
        # arXiv API query
        query = quote(f'au:"{author_name}"')
        url = f"http://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results=50"
        
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Parse XML
        root = ET.fromstring(response.content)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        entries = root.findall('atom:entry', ns)
        cutoff_date = datetime.now() - timedelta(days=days_back)
        
        for entry in entries:
            published_str = entry.find('atom:published', ns).text if entry.find('atom:published', ns) is not None else ''
            
            try:
                published = datetime.fromisoformat(published_str.replace('Z', '+00:00'))
            except:
                published = datetime.now()
            
            if published < cutoff_date:
                continue
            
            # Extract arXiv ID
            id_elem = entry.find('atom:id', ns)
            arxiv_id = id_elem.text.split('/')[-1] if id_elem is not None else ''
            
            title_elem = entry.find('atom:title', ns)
            title = title_elem.text.strip().replace('\n', ' ') if title_elem is not None else ''
            
            summary_elem = entry.find('atom:summary', ns)
            abstract = summary_elem.text.strip() if summary_elem is not None else ''
            
            authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns) if a.find('atom:name', ns) is not None]
            
            pub = {
                'title': title,
                'arxiv_id': arxiv_id,
                'year': published.year,
                'journal': 'arXiv',
                'authors': authors,
                'abstract': abstract,
                'url': f"https://arxiv.org/abs/{arxiv_id}",
                'source': 'arxiv',
            }
            
            if pub['title']:
                publications.append(pub)
        
        # Rate limiting
        time.sleep(1)
        
    except Exception as e:
        print(f"  arXiv query error for {author_name}: {e}", file=sys.stderr)
    
    return publications


def query_biorxiv(author_name: str, days_back: int = 7) -> List[Dict]:
    """Query bioRxiv API for preprints."""
    publications = []
    
    try:
        # bioRxiv API search endpoint
        # Note: bioRxiv's API is limited - we search by author name in title/abstract
        # This is a simplified implementation
        url = f"https://api.biorxiv.org/details/biorxiv/{author_name}/0/50/json"
        
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            data = response.json()
            messages = data.get('collection', [])
            
            cutoff_date = datetime.now() - timedelta(days=days_back)
            
            for msg in messages:
                date_str = msg.get('date', '')
                try:
                    pub_date = datetime.strptime(date_str, '%Y-%m-%d')
                except:
                    continue
                
                if pub_date < cutoff_date:
                    continue
                
                # Check if author name appears in authors
                authors_str = msg.get('authors', '')
                if author_name.lower() not in authors_str.lower():
                    continue
                
                pub = {
                    'title': msg.get('title', ''),
                    'biorxiv_id': msg.get('doi', ''),
                    'doi': msg.get('doi', ''),
                    'year': pub_date.year,
                    'journal': 'bioRxiv',
                    'authors': [a.strip() for a in authors_str.split(';') if a.strip()],
                    'abstract': msg.get('abstract', ''),
                    'url': f"https://www.biorxiv.org/content/{msg.get('doi', '')}",
                    'source': 'biorxiv',
                }
                
                if pub['title']:
                    publications.append(pub)
        
        # Rate limiting
        time.sleep(1)
        
    except Exception as e:
        print(f"  bioRxiv query error for {author_name}: {e}", file=sys.stderr)
    
    return publications


def check_duplicate(publication: Dict, existing_files: List[Path]) -> bool:
    """Check if a publication already exists."""
    doi = publication.get('doi', '')
    arxiv_id = publication.get('arxiv_id', '')
    title = publication.get('title', '').lower()
    
    for file_path in existing_files:
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Check DOI
            if doi and doi in content:
                return True
            
            # Check arXiv ID
            if arxiv_id and arxiv_id in content:
                return True
            
            # Check title (fuzzy)
            if title and title[:50] in content.lower():
                return True
                
        except:
            continue
    
    return False


def main():
    """Main processing function."""
    if len(sys.argv) < 2:
        print("Usage: process-publications.py <faculty_json> [unpaywall_email]", file=sys.stderr)
        sys.exit(1)
    
    faculty_file = Path(sys.argv[1])
    unpaywall_email = sys.argv[2] if len(sys.argv) > 2 else os.getenv('UNPAYWALL_EMAIL', 'github-actions@example.com')
    
    if not faculty_file.exists():
        print(f"Error: Faculty file not found: {faculty_file}", file=sys.stderr)
        sys.exit(1)
    
    with open(faculty_file, 'r') as f:
        faculty_data = json.load(f)
    
    repo_root = Path(__file__).parent.parent.parent
    scripts_dir = Path(__file__).parent
    
    all_publications = []
    new_count = 0
    
    # Get existing publication files for duplicate checking
    existing_files = []
    for lab_dir in repo_root.iterdir():
        if lab_dir.is_dir() and not lab_dir.name.startswith('.'):
            pub_dir = lab_dir / 'publications'
            if pub_dir.exists():
                existing_files.extend(pub_dir.glob('*.md'))
    
    # Process each faculty member
    for faculty in faculty_data.get('faculty', []):
        name = faculty.get('name', '')
        lab_slug = faculty.get('lab_slug', 'unknown')
        orcid = faculty.get('orcid')
        
        if not name:
            continue
        
        print(f"Processing {name} ({lab_slug})...", file=sys.stderr)
        
        # Query APIs
        crossref_pubs = query_crossref(name, orcid)
        arxiv_pubs = query_arxiv(name)
        biorxiv_pubs = query_biorxiv(name)
        
        all_pubs = crossref_pubs + arxiv_pubs + biorxiv_pubs
        
        # Process each publication
        for pub in all_pubs:
            # Check for duplicates
            if check_duplicate(pub, existing_files):
                continue
            
            # Prepare publication data
            pub_data = {
                'title': pub.get('title', ''),
                'doi': pub.get('doi', ''),
                'arxiv_id': pub.get('arxiv_id', ''),
                'biorxiv_id': pub.get('biorxiv_id', ''),
                'year': pub.get('year'),
                'journal': pub.get('journal', ''),
                'authors': pub.get('authors', []),
                'abstract': pub.get('abstract', ''),
                'url': pub.get('url', ''),
                'lab_slug': lab_slug,
                'faculty': [name],
                'tags': ['publication', lab_slug],
                'fulltext_available': False,
                'fulltext_source': 'none',
            }
            
            # Generate title slug
            title_slug = pub_data['title'].lower()
            title_slug = ''.join(c if c.isalnum() or c in '- ' else '' for c in title_slug)
            title_slug = '-'.join(title_slug.split())[:100]
            pub_data['title_slug'] = title_slug
            
            # Try to download PDF
            pdf_path = repo_root / lab_slug / 'publications' / f"{title_slug}.pdf"
            pdf_rel_path = f"{lab_slug}/publications/{title_slug}.pdf"
            
            # Download PDF using download-pdf.py
            # Use tempfile for temp JSON
            temp_dir = Path(tempfile.gettempdir())
            pub_json = temp_dir / f"pub_{title_slug}_{os.getpid()}_{int(time.time())}.json"
            pub_json.write_text(json.dumps(pub_data))
            
            download_result = subprocess.run(
                [sys.executable, str(scripts_dir / 'download-pdf.py'), str(pub_json), unpaywall_email],
                capture_output=True,
                text=True
            )
            
            if download_result.returncode == 0:
                download_info = json.loads(download_result.stdout)
                if download_info.get('downloaded'):
                    pub_data['fulltext_available'] = True
                    pub_data['fulltext_source'] = download_info.get('source', 'unknown')
                    pub_data['pdf_path'] = download_info.get('path')
                    
                    # Convert PDF to markdown
                    if pdf_path.exists():
                        convert_result = subprocess.run(
                            [sys.executable, str(scripts_dir / 'pdf-to-markdown.py'), str(pdf_path)],
                            capture_output=True,
                            text=True
                        )
                        
                        if convert_result.returncode == 0:
                            convert_info = json.loads(convert_result.stdout)
                            if convert_info.get('converted'):
                                md_path = pdf_path.with_suffix('.md')
                                if md_path.exists():
                                    pub_data['fulltext_content'] = md_path.read_text(encoding='utf-8')
            
            # Create publication file
            create_result = subprocess.run(
                [sys.executable, str(scripts_dir / 'create-publication-file.py'), str(pub_json)],
                capture_output=True,
                text=True
            )
            
            if create_result.returncode == 0:
                new_count += 1
                all_publications.append(pub_data)
                print(f"  ✓ Created: {pub_data['title'][:60]}...", file=sys.stderr)
            
            # Cleanup temp file
            if pub_json.exists():
                pub_json.unlink()
    
    # Output summary
    result = {
        'processed': len(all_publications),
        'new_publications': new_count,
    }
    
    print(json.dumps(result))
    print(f"\nProcessed {len(all_publications)} publications, {new_count} new", file=sys.stderr)


if __name__ == '__main__':
    main()

