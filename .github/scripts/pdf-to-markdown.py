#!/usr/bin/env python3
"""
Convert PDF files to Markdown format using pandoc or Python libraries.
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Optional


def convert_with_pandoc(pdf_path: Path, output_path: Path) -> bool:
    """Convert PDF to Markdown using pandoc."""
    try:
        # pandoc command: pandoc input.pdf -t markdown -o output.md
        result = subprocess.run(
            ['pandoc', str(pdf_path), '-t', 'markdown', '-o', str(output_path)],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0 and output_path.exists():
            return True
        else:
            print(f"  Pandoc error: {result.stderr}", file=sys.stderr)
            return False
    except FileNotFoundError:
        print("  Pandoc not found, trying alternative method", file=sys.stderr)
        return False
    except Exception as e:
        print(f"  Pandoc conversion error: {e}", file=sys.stderr)
        return False


def convert_with_pypdf2(pdf_path: Path, output_path: Path) -> bool:
    """Convert PDF to Markdown using PyPDF2 (fallback)."""
    try:
        import PyPDF2
        
        with open(pdf_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            text_content = []
            
            for page_num, page in enumerate(pdf_reader.pages):
                text = page.extract_text()
                if text:
                    text_content.append(f"## Page {page_num + 1}\n\n{text}\n")
            
            if text_content:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(text_content))
                return True
    except ImportError:
        print("  PyPDF2 not available", file=sys.stderr)
        return False
    except Exception as e:
        print(f"  PyPDF2 conversion error: {e}", file=sys.stderr)
        return False


def convert_with_pdfplumber(pdf_path: Path, output_path: Path) -> bool:
    """Convert PDF to Markdown using pdfplumber (better for academic papers)."""
    try:
        import pdfplumber
        
        text_content = []
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    text_content.append(f"## Page {page_num + 1}\n\n{text}\n")
        
        if text_content:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(text_content))
            return True
    except ImportError:
        print("  pdfplumber not available", file=sys.stderr)
        return False
    except Exception as e:
        print(f"  pdfplumber conversion error: {e}", file=sys.stderr)
        return False


def main():
    """Main function to convert PDF to Markdown."""
    if len(sys.argv) < 2:
        print("Usage: pdf-to-markdown.py <pdf_path> [output_path]", file=sys.stderr)
        sys.exit(1)
    
    pdf_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else pdf_path.with_suffix('.md')
    
    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)
    
    # Try conversion methods in order of preference
    converted = False
    
    # 1. Try pandoc (best quality)
    if convert_with_pandoc(pdf_path, output_path):
        converted = True
        method = 'pandoc'
    
    # 2. Try pdfplumber (good for academic papers)
    elif convert_with_pdfplumber(pdf_path, output_path):
        converted = True
        method = 'pdfplumber'
    
    # 3. Try PyPDF2 (fallback)
    elif convert_with_pypdf2(pdf_path, output_path):
        converted = True
        method = 'pypdf2'
    
    # Output result
    result = {
        'converted': converted,
        'method': method if converted else None,
        'output_path': str(output_path) if converted else None,
    }
    
    print(json.dumps(result))


if __name__ == '__main__':
    main()

