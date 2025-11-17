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
import re
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timedelta, timezone
from urllib.parse import quote


def normalize_author_name(name: str) -> str:
    """Normalize author name for matching."""
    # Remove extra spaces, convert to lowercase
    name = ' '.join(name.split()).lower()
    return name


def author_name_matches(author_name: str, author_list: List[str], threshold: float = 0.7) -> bool:
    """
    Check if author_name appears in author_list with fuzzy matching.
    Returns True if a reasonable match is found.
    """
    normalized_search = normalize_author_name(author_name)
    search_parts = normalized_search.split()
    
    if len(search_parts) < 2:
        # If name is too short, do simple substring match
        return any(normalized_search in normalize_author_name(a) for a in author_list)
    
    # Extract last name (usually most distinctive)
    last_name = search_parts[-1]
    
    # Check each author in the list
    for author in author_list:
        normalized_author = normalize_author_name(author)
        author_parts = normalized_author.split()
        
        # Must have last name match
        if last_name not in author_parts:
            continue
        
        # Check if first name or initial matches
        if len(search_parts) > 1:
            first_name = search_parts[0]
            # Match first name or first initial
            if first_name in author_parts or (len(first_name) == 1 and author_parts[0].startswith(first_name)):
                return True
        
        # If last name matches and it's a distinctive name, accept it
        if len(last_name) >= 5:  # Longer last names are more distinctive
            return True
    
    return False


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
            authors = [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in item.get('author', [])]
            
            # Filter: only include if author name matches
            if not author_name_matches(author_name, authors):
                continue
            
            pub = {
                'title': item.get('title', [''])[0] if item.get('title') else '',
                'doi': item.get('DOI', ''),
                'year': item.get('published', {}).get('date-parts', [[None]])[0][0] if item.get('published', {}).get('date-parts') else None,
                'journal': item.get('container-title', [''])[0] if item.get('container-title') else '',
                'authors': authors,
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
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_back)
        
        for entry in entries:
            published_str = entry.find('atom:published', ns).text if entry.find('atom:published', ns) is not None else ''
            
            try:
                # Handle timezone-aware datetime
                if published_str.endswith('Z'):
                    published = datetime.fromisoformat(published_str.replace('Z', '+00:00'))
                else:
                    published = datetime.fromisoformat(published_str)
                # Ensure timezone-aware
                if published.tzinfo is None:
                    published = published.replace(tzinfo=timezone.utc)
            except Exception as e:
                # Skip entries with invalid dates
                continue
            
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
            
            # Filter: only include if author name matches
            if not author_name_matches(author_name, authors):
                continue
            
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


def query_pubmed(author_name: str, days_back: int = 7) -> List[Dict]:
    """Query PubMed API for publications."""
    publications = []
    
    try:
        # Split author name into parts
        name_parts = author_name.split()
        if len(name_parts) < 2:
            return publications
        
        # PubMed format: LastName FirstName[Author]
        last_name = name_parts[-1]
        first_name = name_parts[0]
        
        # Build query: author name + date filter
        cutoff_date = datetime.now() - timedelta(days=days_back)
        date_str = cutoff_date.strftime('%Y/%m/%d')
        
        # PubMed query format
        query = quote(f'{last_name} {first_name}[Author] AND {date_str}[PDat] : {datetime.now().strftime("%Y/%m/%d")}[PDat]')
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmax=50&retmode=json"
        
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        search_data = response.json()
        
        pmids = search_data.get('esearchresult', {}).get('idlist', [])
        
        if not pmids:
            return publications
        
        # Fetch details for each PMID
        pmids_str = ','.join(pmids[:20])  # Limit to 20 at a time
        fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmids_str}&retmode=xml"
        
        fetch_response = requests.get(fetch_url, timeout=30)
        fetch_response.raise_for_status()
        
        # Parse XML - PubMed XML uses namespaces
        root = ET.fromstring(fetch_response.content)
        
        # Find namespace URI from root element
        ns_uri = ''
        if root.tag.startswith('{'):
            ns_uri = root.tag[1:].split('}')[0]
        
        # Define namespace dict
        ns = {'pubmed': ns_uri} if ns_uri else {}
        
        # Helper to find elements with or without namespace
        def find_elem(parent, path):
            if ns_uri:
                return parent.find(path.replace('pubmed:', f'{{{ns_uri}}}'), ns)
            else:
                return parent.find(path.replace('pubmed:', ''))
        
        def findall_elems(parent, path):
            if ns_uri:
                return parent.findall(path.replace('pubmed:', f'{{{ns_uri}}}'), ns)
            else:
                return parent.findall(path.replace('pubmed:', ''))
        
        articles = findall_elems(root, './/pubmed:PubmedArticle')
        
        for article in articles:
            try:
                # Extract title
                title_elem = find_elem(article, './/pubmed:ArticleTitle')
                title = title_elem.text if title_elem is not None and title_elem.text else ''
                
                # Extract authors
                authors = []
                author_list = findall_elems(article, './/pubmed:Author')
                for author in author_list:
                    last = find_elem(author, 'pubmed:LastName')
                    first = find_elem(author, 'pubmed:ForeName')
                    if last is not None and last.text:
                        author_name_full = f"{first.text if first is not None and first.text else ''} {last.text}".strip()
                        authors.append(author_name_full)
                
                # Filter: only include if author name matches
                if not author_name_matches(author_name, authors):
                    continue
                
                # Extract abstract
                abstract_elem = find_elem(article, './/pubmed:AbstractText')
                abstract = abstract_elem.text if abstract_elem is not None and abstract_elem.text else ''
                
                # Extract PMID
                pmid_elem = find_elem(article, './/pubmed:PMID')
                pmid = pmid_elem.text if pmid_elem is not None else ''
                
                # Extract journal
                journal_elem = find_elem(article, './/pubmed:Journal/pubmed:Title')
                journal = journal_elem.text if journal_elem is not None else ''
                
                # Extract year
                year_elem = find_elem(article, './/pubmed:PubDate/pubmed:Year')
                year = int(year_elem.text) if year_elem is not None and year_elem.text and year_elem.text.isdigit() else None
                
                # Extract DOI if available
                doi_elems = findall_elems(article, './/pubmed:ELocationID')
                doi = ''
                for doi_elem in doi_elems:
                    if doi_elem.get('EIdType') == 'doi':
                        doi = doi_elem.text if doi_elem.text else ''
                        break
                
                pub = {
                    'title': title,
                    'doi': doi,
                    'pmid': pmid,
                    'year': year,
                    'journal': journal,
                    'authors': authors,
                    'abstract': abstract,
                    'url': f"https://pubmed.ncbi.nlm.nih.gov/{pmid}" if pmid else '',
                    'source': 'pubmed',
                }
                
                if pub['title']:
                    publications.append(pub)
            
            except Exception as e:
                continue
        
        # Rate limiting
        time.sleep(1)
        
    except Exception as e:
        print(f"  PubMed query error for {author_name}: {e}", file=sys.stderr)
    
    return publications


def query_semantic_scholar(author_name: str, orcid: Optional[str] = None, days_back: int = 7) -> List[Dict]:
    """Query Semantic Scholar API for publications."""
    publications = []
    
    try:
        # Semantic Scholar API
        # First, search for author
        search_query = quote(author_name)
        search_url = f"https://api.semanticscholar.org/graph/v1/author/search?query={search_query}&limit=5"
        
        headers = {
            'User-Agent': 'Academic Publication Tracker (github-actions@example.com)',
            'Accept': 'application/json'
        }
        
        search_response = requests.get(search_url, headers=headers, timeout=30)
        search_response.raise_for_status()
        search_data = search_response.json()
        
        author_ids = []
        for author in search_data.get('data', []):
            # Match by name similarity
            if author_name_matches(author_name, [author.get('name', '')]):
                author_ids.append(author.get('authorId'))
        
        if not author_ids:
            return publications
        
        # Use first matching author
        author_id = author_ids[0]
        
        # Get author's papers
        cutoff_date = datetime.now() - timedelta(days=days_back)
        papers_url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}/papers?fields=title,authors,year,abstract,doi,url,journal&limit=50"
        
        papers_response = requests.get(papers_url, headers=headers, timeout=30)
        papers_response.raise_for_status()
        papers_data = papers_response.json()
        
        for paper in papers_data.get('data', []):
            # Filter by date
            paper_year = paper.get('year')
            if paper_year and paper_year < cutoff_date.year:
                continue
            
            # Extract authors
            authors = [a.get('name', '') for a in paper.get('authors', [])]
            
            # Filter: only include if author name matches
            if not author_name_matches(author_name, authors):
                continue
            
            pub = {
                'title': paper.get('title', ''),
                'doi': paper.get('doi', ''),
                'year': paper_year,
                'journal': paper.get('journal', {}).get('name', '') if isinstance(paper.get('journal'), dict) else paper.get('journal', ''),
                'authors': authors,
                'abstract': paper.get('abstract', ''),
                'url': paper.get('url', ''),
                'source': 'semantic_scholar',
            }
            
            if pub['title']:
                publications.append(pub)
        
        # Rate limiting
        time.sleep(1)
        
    except Exception as e:
        print(f"  Semantic Scholar query error for {author_name}: {e}", file=sys.stderr)
    
    return publications


def deduplicate_publications(publications: List[Dict]) -> List[Dict]:
    """Remove duplicate publications from a list based on DOI, arXiv ID, or title similarity."""
    seen = set()
    deduplicated = []
    
    for pub in publications:
        doi = pub.get('doi', '').lower().strip()
        arxiv_id = pub.get('arxiv_id', '').lower().strip()
        pmid = pub.get('pmid', '').lower().strip()
        title = pub.get('title', '').lower().strip()
        
        # Create signature for this publication
        signature = None
        
        # Prefer DOI as unique identifier
        if doi:
            signature = f"doi:{doi}"
        # Then arXiv ID
        elif arxiv_id:
            signature = f"arxiv:{arxiv_id}"
        # Then PMID
        elif pmid:
            signature = f"pmid:{pmid}"
        # Fall back to title (first 100 chars)
        elif title:
            signature = f"title:{title[:100]}"
        
        if signature and signature not in seen:
            seen.add(signature)
            deduplicated.append(pub)
        elif not signature:
            # If no signature, include it (shouldn't happen)
            deduplicated.append(pub)
    
    return deduplicated


def check_duplicate(publication: Dict, existing_files: List[Path]) -> bool:
    """Check if a publication already exists in existing files."""
    doi = publication.get('doi', '')
    arxiv_id = publication.get('arxiv_id', '')
    pmid = publication.get('pmid', '')
    title = publication.get('title', '').lower()
    
    for file_path in existing_files:
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Check DOI
            if doi and doi.lower() in content.lower():
                return True
            
            # Check arXiv ID
            if arxiv_id and arxiv_id.lower() in content.lower():
                return True
            
            # Check PMID
            if pmid and pmid.lower() in content.lower():
                return True
            
            # Check title (fuzzy)
            if title and len(title) > 20 and title[:50] in content.lower():
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
        
        # Query APIs - prioritize ORCID-based queries
        all_pubs = []
        
        # Crossref (best with ORCID)
        crossref_pubs = query_crossref(name, orcid)
        all_pubs.extend(crossref_pubs)
        
        # Semantic Scholar (good author matching)
        semantic_pubs = query_semantic_scholar(name, orcid)
        all_pubs.extend(semantic_pubs)
        
        # PubMed (good for neuroscience/biology)
        pubmed_pubs = query_pubmed(name)
        all_pubs.extend(pubmed_pubs)
        
        # arXiv (with improved filtering)
        arxiv_pubs = query_arxiv(name)
        all_pubs.extend(arxiv_pubs)
        
        # bioRxiv
        biorxiv_pubs = query_biorxiv(name)
        all_pubs.extend(biorxiv_pubs)
        
        # Deduplicate publications from different APIs
        all_pubs = deduplicate_publications(all_pubs)
        
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
                'pmid': pub.get('pmid', ''),
                'year': pub.get('year'),
                'journal': pub.get('journal', ''),
                'authors': pub.get('authors', []),
                'abstract': pub.get('abstract', ''),
                'url': pub.get('url', ''),
                'source': pub.get('source', 'unknown'),
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

