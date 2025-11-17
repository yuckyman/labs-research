#!/usr/bin/env python3
"""
Create individual markdown files with YAML frontmatter for each publication.
Compatible with Obsidian Bases.
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    if not text:
        return 'publication'
    
    # Remove special characters, keep alphanumeric, spaces, and hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces and multiple hyphens with single hyphen
    text = re.sub(r'[-\s]+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    # Limit length
    text = text[:100]
    return text.lower() or 'publication'


def escape_yaml_string(text: str) -> str:
    """Escape special characters for YAML strings."""
    if not text:
        return ''
    
    # Replace newlines with spaces for single-line strings
    text = text.replace('\n', ' ').replace('\r', ' ')
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Escape quotes
    text = text.replace('"', '\\"')
    return text.strip()


def format_yaml_value(value) -> str:
    """Format a value for YAML output."""
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, list):
        if not value:
            return '[]'
        items = []
        for item in value:
            if isinstance(item, str):
                items.append(f'- "{escape_yaml_string(item)}"')
            else:
                items.append(f'- {format_yaml_value(item)}')
        return '\n'.join(items)
    elif isinstance(value, str):
        # Use block scalar for long strings (abstracts)
        if len(value) > 100 or '\n' in value:
            # Escape and use literal block scalar
            escaped = value.replace('\\', '\\\\').replace('\n', '\n  ')
            return f'|\n  {escaped}'
        else:
            return f'"{escape_yaml_string(value)}"'
    else:
        return str(value)


def create_publication_file(publication: Dict, repo_root: Path) -> Path:
    """Create a markdown file for a publication with YAML frontmatter."""
    lab_slug = publication.get('lab_slug', 'unknown')
    title = publication.get('title', 'Untitled')
    title_slug = publication.get('title_slug', slugify(title))
    
    # Determine output directory
    output_dir = repo_root / lab_slug / 'publications'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{title_slug}.md"
    
    # Build YAML frontmatter
    frontmatter_lines = ['---']
    
    # Required fields
    frontmatter_lines.append(f'title: {format_yaml_value(title)}')
    
    # Authors
    authors = publication.get('authors', [])
    if authors:
        frontmatter_lines.append('authors:')
        for author in authors:
            frontmatter_lines.append(f'  - "{escape_yaml_string(author)}"')
    
    # Year
    year = publication.get('year')
    if year:
        frontmatter_lines.append(f'year: {year}')
    
    # Journal
    journal = publication.get('journal')
    if journal:
        frontmatter_lines.append(f'journal: {format_yaml_value(journal)}')
    
    # DOI
    doi = publication.get('doi')
    if doi:
        frontmatter_lines.append(f'doi: "{doi}"')
    
    # arXiv ID
    arxiv_id = publication.get('arxiv_id')
    if arxiv_id:
        frontmatter_lines.append(f'arxiv_id: "{arxiv_id}"')
    
    # bioRxiv ID
    biorxiv_id = publication.get('biorxiv_id')
    if biorxiv_id:
        frontmatter_lines.append(f'biorxiv_id: "{biorxiv_id}"')
    
    # URL
    url = publication.get('url')
    if url:
        frontmatter_lines.append(f'url: "{url}"')
    
    # PDF path (relative to repo root)
    pdf_path = publication.get('pdf_path')
    if pdf_path:
        frontmatter_lines.append(f'pdf_path: "{pdf_path}"')
    
    # Lab
    frontmatter_lines.append(f'lab: "{lab_slug}"')
    
    # Faculty
    faculty = publication.get('faculty', [])
    if faculty:
        frontmatter_lines.append('faculty:')
        for f in faculty:
            frontmatter_lines.append(f'  - "{escape_yaml_string(f)}"')
    
    # Tags
    tags = publication.get('tags', ['publication', lab_slug])
    if tags:
        frontmatter_lines.append('tags:')
        for tag in tags:
            frontmatter_lines.append(f'  - "{tag}"')
    
    # Abstract (only if fulltext not available)
    fulltext_available = publication.get('fulltext_available', False)
    abstract = publication.get('abstract')
    if abstract and not fulltext_available:
        frontmatter_lines.append(f'abstract: {format_yaml_value(abstract)}')
    
    # Fulltext metadata
    frontmatter_lines.append(f'fulltext_available: {str(fulltext_available).lower()}')
    
    fulltext_source = publication.get('fulltext_source', 'none')
    frontmatter_lines.append(f'fulltext_source: "{fulltext_source}"')
    
    # Add created date
    frontmatter_lines.append(f'created: "{datetime.now().isoformat()}"')
    
    frontmatter_lines.append('---')
    frontmatter = '\n'.join(frontmatter_lines)
    
    # Build content
    content_lines = [frontmatter, '']
    
    # Add title as heading
    content_lines.append(f'# {title}')
    content_lines.append('')
    
    # Add fulltext content if available
    fulltext_content = publication.get('fulltext_content')
    if fulltext_content:
        content_lines.append('## Full Text')
        content_lines.append('')
        content_lines.append(fulltext_content)
        content_lines.append('')
    elif abstract:
        # Add abstract if no fulltext
        content_lines.append('## Abstract')
        content_lines.append('')
        content_lines.append(abstract)
        content_lines.append('')
    
    # Add links section
    content_lines.append('## Links')
    content_lines.append('')
    if doi:
        content_lines.append(f'- DOI: [{doi}](https://doi.org/{doi})')
    if arxiv_id:
        arxiv_id_clean = arxiv_id.replace('arXiv:', '')
        content_lines.append(f'- arXiv: [arXiv:{arxiv_id_clean}](https://arxiv.org/abs/{arxiv_id_clean})')
    if biorxiv_id:
        content_lines.append(f'- bioRxiv: [{biorxiv_id}](https://www.biorxiv.org/content/{biorxiv_id})')
    if url:
        content_lines.append(f'- URL: [Link]({url})')
    if pdf_path:
        content_lines.append(f'- PDF: [[{pdf_path}]]')
    content_lines.append('')
    
    # Add faculty links
    if faculty:
        content_lines.append('## Faculty')
        content_lines.append('')
        for f in faculty:
            faculty_slug = slugify(f)
            content_lines.append(f'- [[{lab_slug}/faculty#{faculty_slug}|{f}]]')
        content_lines.append('')
    
    # Write file
    content = '\n'.join(content_lines)
    output_path.write_text(content, encoding='utf-8')
    
    return output_path


def main():
    """Main function to create publication files."""
    if len(sys.argv) < 2:
        print("Usage: create-publication-file.py <publication_json>", file=sys.stderr)
        sys.exit(1)
    
    pub_file = Path(sys.argv[1])
    
    if not pub_file.exists():
        print(f"Error: Publication file not found: {pub_file}", file=sys.stderr)
        sys.exit(1)
    
    with open(pub_file, 'r') as f:
        publication = json.load(f)
    
    # Determine repo root (3 levels up from scripts/)
    repo_root = Path(__file__).parent.parent.parent
    
    # Generate title slug if not present
    if 'title_slug' not in publication:
        title = publication.get('title', 'Untitled')
        publication['title_slug'] = slugify(title)
    
    # Create the publication file
    output_path = create_publication_file(publication, repo_root)
    
    result = {
        'created': True,
        'path': str(output_path.relative_to(repo_root)),
    }
    
    print(json.dumps(result))


if __name__ == '__main__':
    main()

