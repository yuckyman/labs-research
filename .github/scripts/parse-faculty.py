#!/usr/bin/env python3
"""
Parse faculty.md files from all lab directories and extract faculty information.
Outputs JSON with faculty names, ORCID IDs, lab associations, and metadata.
"""

import os
import re
import json
import sys
import yaml
from pathlib import Path
from typing import List, Dict, Optional


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def extract_orcid(text: str) -> Optional[str]:
    """Extract ORCID ID from text."""
    # Match ORCID format: 0000-0000-0000-0000
    orcid_pattern = r'\d{4}-\d{4}-\d{4}-\d{4}'
    match = re.search(orcid_pattern, text)
    if match:
        return match.group(0)
    return None


def is_template_entry(name: str) -> bool:
    """Check if a faculty name is a template placeholder."""
    template_patterns = [
        r'\[.*\]',  # [Faculty Name], [To be updated]
        r'^\[',     # Starts with [
        r'To be updated',
        r'^N/A',
        r'^TBD',
    ]
    for pattern in template_patterns:
        if re.search(pattern, name, re.IGNORECASE):
            return True
    return False


def parse_frontmatter(content: str) -> Dict:
    """Extract YAML frontmatter from markdown content."""
    frontmatter = {}
    
    # Check for YAML frontmatter (between --- markers)
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if frontmatter_match:
        try:
            frontmatter = yaml.safe_load(frontmatter_match.group(1)) or {}
        except yaml.YAMLError:
            # If YAML parsing fails, return empty dict
            pass
    
    return frontmatter


def parse_faculty_file(faculty_path: Path, lab_name: str) -> List[Dict]:
    """Parse a single faculty.md file and extract faculty information."""
    faculty_list = []
    
    if not faculty_path.exists():
        return faculty_list
    
    content = faculty_path.read_text(encoding='utf-8')
    
    # Check file-level draft status
    frontmatter = parse_frontmatter(content)
    if frontmatter.get('draft', False) is True:
        print(f"  Skipping {lab_name}/faculty.md (marked as draft)", file=sys.stderr)
        return faculty_list
    
    # Remove frontmatter from content for processing
    content_without_frontmatter = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL, count=1)
    if not content_without_frontmatter.strip():
        content_without_frontmatter = content
    
    # Split by ### headings (faculty entries)
    sections = re.split(r'^###\s+(.+)$', content_without_frontmatter, flags=re.MULTILINE)
    
    # Process pairs: [name, content, name, content, ...]
    for i in range(1, len(sections), 2):
        if i + 1 >= len(sections):
            break
            
        name = sections[i].strip()
        entry_content = sections[i + 1]
        
        # Skip template entries
        if is_template_entry(name):
            continue
        
        # Check if this individual entry is marked as draft
        # Look for **Draft:** true or draft: true in the entry
        draft_match = re.search(r'\*\*Draft:\*\*\s*(true|yes)', entry_content, re.IGNORECASE)
        if draft_match:
            print(f"  Skipping {name} (marked as draft)", file=sys.stderr)
            continue
        
        content = entry_content
        
        # Extract metadata from content
        faculty_info = {
            'name': name,
            'lab': lab_name,
            'lab_slug': slugify(lab_name),
        }
        
        # Extract ORCID
        orcid = extract_orcid(content)
        if orcid:
            faculty_info['orcid'] = orcid
        
        # Extract email
        email_match = re.search(r'\*\*Email:\*\*\s*([^\n]+)', content)
        if email_match:
            email = email_match.group(1).strip()
            if email and not is_template_entry(email):
                faculty_info['email'] = email
        
        # Extract position
        position_match = re.search(r'\*\*Position:\*\*\s*([^\n]+)', content)
        if position_match:
            position = position_match.group(1).strip()
            if position and not is_template_entry(position):
                faculty_info['position'] = position
        
        # Extract website
        website_match = re.search(r'\*\*Website:\*\*\s*([^\n]+)', content)
        if website_match:
            website = website_match.group(1).strip()
            if website and not is_template_entry(website) and website.startswith('http'):
                faculty_info['website'] = website
        
        faculty_list.append(faculty_info)
    
    return faculty_list


def main():
    """Main function to parse all faculty.md files."""
    repo_root = Path(__file__).parent.parent.parent
    labs_dir = repo_root
    
    all_faculty = []
    
    # Find all lab directories (subdirectories with faculty.md)
    for item in labs_dir.iterdir():
        if not item.is_dir():
            continue
        
        # Skip hidden directories and special directories
        if item.name.startswith('.') or item.name in ['publications', 'tracking']:
            continue
        
        faculty_path = item / 'faculty.md'
        if faculty_path.exists():
            lab_name = item.name
            print(f"Parsing faculty from {lab_name}...", file=sys.stderr)
            faculty_list = parse_faculty_file(faculty_path, lab_name)
            all_faculty.extend(faculty_list)
            print(f"  Found {len(faculty_list)} faculty members", file=sys.stderr)
    
    # Output JSON
    output = {
        'faculty': all_faculty,
        'total': len(all_faculty),
    }
    
    print(json.dumps(output, indent=2))
    print(f"\nTotal faculty members found: {len(all_faculty)}", file=sys.stderr)


if __name__ == '__main__':
    main()

