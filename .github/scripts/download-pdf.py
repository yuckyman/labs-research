#!/usr/bin/env python3
"""
Download PDFs from various sources: arXiv, bioRxiv, and open access via Unpaywall.
"""

import os
import sys
import json
import requests
import time
from pathlib import Path
from typing import Optional, Dict
from urllib.parse import urlparse


def download_file(url: str, output_path: Path, timeout: int = 30) -> bool:
    """Download a file from URL to output path."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; AcademicBot/1.0; +https://github.com/academic/publication-tracker)'
        }
        response = requests.get(url, headers=headers, timeout=timeout, stream=True)
        response.raise_for_status()
        
        # Check if it's actually a PDF
        content_type = response.headers.get('content-type', '').lower()
        if 'pdf' not in content_type and not url.endswith('.pdf'):
            # Check first bytes for PDF magic number
            first_bytes = response.content[:4]
            if first_bytes != b'%PDF':
                print(f"  Warning: {url} doesn't appear to be a PDF", file=sys.stderr)
                return False
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return True
    except Exception as e:
        print(f"  Error downloading {url}: {e}", file=sys.stderr)
        return False


def download_arxiv_pdf(arxiv_id: str, output_path: Path) -> bool:
    """Download PDF from arXiv."""
    # Remove 'arXiv:' prefix if present
    arxiv_id = arxiv_id.replace('arXiv:', '').strip()
    
    # arXiv PDF URL format: https://arxiv.org/pdf/{id}.pdf
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    print(f"  Downloading arXiv PDF: {arxiv_id}", file=sys.stderr)
    return download_file(url, output_path)


def download_biorxiv_pdf(doi: str, output_path: Path) -> bool:
    """Download PDF from bioRxiv."""
    # bioRxiv DOI format: 10.1101/2023.01.01.123456
    # PDF URL: https://www.biorxiv.org/content/{doi}v{version}.full.pdf
    # We'll try version 1 first
    
    # Clean DOI - remove any prefixes
    clean_doi = doi.replace('doi:', '').replace('DOI:', '').strip()
    
    # Try version 1 (most common)
    url = f"https://www.biorxiv.org/content/{clean_doi}v1.full.pdf"
    print(f"  Downloading bioRxiv PDF: {clean_doi}", file=sys.stderr)
    
    if download_file(url, output_path):
        return True
    
    # If version 1 fails, try without version (latest)
    url = f"https://www.biorxiv.org/content/{clean_doi}.full.pdf"
    return download_file(url, output_path)


def check_unpaywall(doi: str, email: str) -> Optional[Dict]:
    """Check Unpaywall API for open access PDF."""
    if not doi or not doi.startswith('10.'):
        return None
    
    try:
        url = f"https://api.unpaywall.org/v2/{doi}?email={email}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Check if open access PDF is available
        if data.get('is_oa', False):
            best_oa = data.get('best_oa_location')
            if best_oa and best_oa.get('url_for_pdf'):
                return {
                    'url': best_oa['url_for_pdf'],
                    'license': best_oa.get('license'),
                    'version': best_oa.get('version'),
                }
    except Exception as e:
        print(f"  Unpaywall check failed for {doi}: {e}", file=sys.stderr)
    
    return None


def download_unpaywall_pdf(oa_info: Dict, output_path: Path) -> bool:
    """Download PDF from Unpaywall open access URL."""
    url = oa_info['url']
    print(f"  Downloading open access PDF from Unpaywall", file=sys.stderr)
    return download_file(url, output_path)


def main():
    """Main function to download PDFs based on publication data."""
    if len(sys.argv) < 2:
        print("Usage: download-pdf.py <publication_json> [unpaywall_email]", file=sys.stderr)
        sys.exit(1)
    
    pub_file = Path(sys.argv[1])
    unpaywall_email = sys.argv[2] if len(sys.argv) > 2 else os.getenv('UNPAYWALL_EMAIL', 'github-actions@example.com')
    
    if not pub_file.exists():
        print(f"Error: Publication file not found: {pub_file}", file=sys.stderr)
        sys.exit(1)
    
    with open(pub_file, 'r') as f:
        publication = json.load(f)
    
    lab_slug = publication.get('lab_slug', 'unknown')
    title_slug = publication.get('title_slug', 'publication')
    
    # Determine output path
    repo_root = Path(__file__).parent.parent.parent
    output_dir = repo_root / lab_slug / 'publications'
    output_path = output_dir / f"{title_slug}.pdf"
    
    # Try different sources in order
    downloaded = False
    source = None
    
    # 1. Try arXiv
    arxiv_id = publication.get('arxiv_id')
    if arxiv_id and not downloaded:
        if download_arxiv_pdf(arxiv_id, output_path):
            downloaded = True
            source = 'arxiv'
    
    # 2. Try bioRxiv
    biorxiv_id = publication.get('biorxiv_id')
    doi = publication.get('doi', '')
    if biorxiv_id and not downloaded:
        if download_biorxiv_pdf(biorxiv_id, output_path):
            downloaded = True
            source = 'biorxiv'
    
    # 3. Try Unpaywall for open access
    if doi and not downloaded:
        oa_info = check_unpaywall(doi, unpaywall_email)
        if oa_info:
            if download_unpaywall_pdf(oa_info, output_path):
                downloaded = True
                source = 'unpaywall'
    
    # Output result
    result = {
        'downloaded': downloaded,
        'source': source,
        'path': str(output_path.relative_to(repo_root)) if downloaded else None,
    }
    
    print(json.dumps(result))
    
    # Rate limiting
    time.sleep(1)


if __name__ == '__main__':
    main()

