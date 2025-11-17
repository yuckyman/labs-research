# Enhanced Publication Tracking with PDFs and Obsidian Bases

## Overview

Transform the existing publication tracking workflow to:

- Parse all `faculty.md` files across lab directories to extract faculty names
- Download full-text PDFs from arXiv, bioRxiv, and open access sources (via Unpaywall API)
- Convert PDFs to markdown for machine readability
- Create individual markdown files with YAML frontmatter for each publication (compatible with Obsidian Bases)
- Include abstracts only when fulltext isn't available
- Store files in `{lab-name}/publications/{title-slug}.pdf` and `{lab-name}/publications/{title-slug}.md`

## Implementation Plan

### 1. Faculty Parsing Module

**File:** `.github/scripts/parse-faculty.py` (or bash script)

- Scan all subdirectories in `labs/` for `faculty.md` files
- Extract faculty names from markdown headings (`### [Faculty Name]`)
- Extract metadata (ORCID, email, position) when available
- Map each faculty member to their lab directory
- Output JSON/YAML config for publication queries

**Key parsing logic:**

- Match pattern: `### [Faculty Name]` headings
- Skip template entries (e.g., `[Faculty Name]`, `[To be updated]`)
- Extract ORCID IDs for better API queries
- Handle name variations (e.g., "John-Dylan Haynes" vs "John Dylan Haynes")

### 2. Enhanced Publication Querying

**Modify:** `.github/workflows/track-publications.yml`

- Replace hardcoded author list with dynamic parsing from faculty.md files
- Query Crossref API using author names + ORCID when available
- Query arXiv API for preprints
- Query bioRxiv API for biology preprints
- Use Unpaywall API to check for open access PDFs (requires email for API key)

**APIs to integrate:**

- Crossref: `https://api.crossref.org/works?query.author=...`
- arXiv: `http://export.arxiv.org/api/query?search_query=au:...`
- bioRxiv: `https://api.biorxiv.org/details/{server}/{doi}` or RSS feeds
- Unpaywall: `https://api.unpaywall.org/v2/{doi}?email=...` (free, requires email)

### 3. PDF Download and Conversion

**New step in workflow:**

- **Download PDFs:**
                                                                - arXiv: Direct download from `https://arxiv.org/pdf/{arxiv_id}.pdf`
                                                                - bioRxiv: Download from `https://www.biorxiv.org/content/{doi}v{version}.full.pdf`
                                                                - Open access via Unpaywall: Use `best_oa_location.url` from API response
                                                                - Store in `{lab-name}/publications/{title-slug}.pdf`

- **Convert PDF to Markdown:**
                                                                - Use `pandoc` (install in workflow: `sudo apt-get install pandoc`)
                                                                - Alternative: Python library `pdf2md` or `marker` (more advanced, better for academic papers)
                                                                - Command: `pandoc {pdf_file} -t markdown -o {output.md}` or use Python script
                                                                - Store converted markdown in `{lab-name}/publications/{title-slug}.md`

**Note on Sci-Hub:** While programmatic access to Sci-Hub is technically possible (via domains like `sci-hub.se` and DOI-based URLs), it raises significant legal and ethical concerns. Sci-Hub operates by bypassing publisher paywalls, which violates copyright laws in many jurisdictions. Additionally, Sci-Hub domains are frequently blocked and change regularly, making it unreliable for automated workflows. We'll stick with legal open access sources only.

### 4. Individual Publication Files with YAML Frontmatter

**New file structure:** `{lab-name}/publications/{title-slug}.md`

Each publication gets its own markdown file with:

```yaml
---
title: "Publication Title"
authors:
 - "Author One"
 - "Author Two"
year: 2025
journal: "Journal Name"
doi: "10.xxxx/xxxxx"
arxiv_id: "2301.12345"  # if applicable
biorxiv_id: "2023.01.01.123456"  # if applicable
url: "https://doi.org/10.xxxx/xxxxx"
pdf_path: "publications/title-slug.pdf"
lab: "max-planck-tubingen"
faculty:
 - "Faculty Name"
tags:
 - "publication"
 - "max-planck-tubingen"
 - "computational-neuroscience"
abstract: |
  Abstract text here (only if fulltext not available)
fulltext_available: true  # or false
fulltext_source: "arxiv"  # arxiv, biorxiv, unpaywall, none
---
```

**Content:**

- If PDF converted successfully: Include converted markdown content
- If only abstract available: Include abstract in frontmatter and body
- Add metadata links, citations, etc.

### 5. Abstract Extraction

- Extract abstracts from Crossref API response (`abstract` field)
- Extract abstracts from arXiv API (`summary` field)
- Extract abstracts from bioRxiv API
- Only include in YAML frontmatter if `fulltext_available: false`

### 6. Workflow Updates

**Modify:** `.github/workflows/track-publications.yml`

**New steps:**

1. Parse all faculty.md files → generate faculty list
2. For each faculty member:

                                                                                                - Query APIs (Crossref, arXiv, bioRxiv)
                                                                                                - Check Unpaywall for open access
                                                                                                - Download PDFs when available
                                                                                                - Convert PDFs to markdown
                                                                                                - Extract abstracts if needed
                                                                                                - Create individual publication markdown files
                                                                                                - Check for duplicates (by DOI/arXiv ID)

3. Commit new publication files

**Dependencies to install:**

- `pandoc` (for PDF conversion)
- Python packages: `requests`, `PyPDF2` or `pdfplumber`, `markdown` (if using Python for conversion)
- Or use `marker` library for better academic PDF parsing

### 7. Obsidian Bases Integration

**Documentation:** Create `OBSIDIAN_BASES_SETUP.md`

- Explain how to create Bases in Obsidian that filter publications by lab/faculty
- Example base configuration for viewing publications
- How to link publications to faculty members
- Filtering and sorting examples

## Files to Create/Modify

1. **`.github/workflows/track-publications.yml`** - Major refactor
2. **`.github/scripts/parse-faculty.py`** - New script for parsing faculty.md
3. **`.github/scripts/download-pdf.py`** - New script for PDF downloads
4. **`.github/scripts/pdf-to-markdown.py`** - New script for PDF conversion
5. **`.github/scripts/create-publication-file.py`** - New script to generate publication markdown files
6. **`OBSIDIAN_BASES_SETUP.md`** - Documentation for Obsidian Bases setup

## Considerations

- **Rate limiting:** Add delays between API calls to respect rate limits
- **File size:** PDFs can be large; consider Git LFS or separate storage
- **PDF quality:** Academic PDFs vary in quality; conversion may need refinement
- **Name matching:** Handle author name variations (e.g., "J. Smith" vs "John Smith")
- **Unpaywall API:** Requires email address (free tier available)
- **Error handling:** Gracefully handle failed downloads/conversions

## Testing Strategy

- Test with a single lab/faculty member first
- Verify PDF downloads work for arXiv papers
- Test PDF to markdown conversion quality
- Verify YAML frontmatter structure works with Obsidian Bases
- Check duplicate detection logic