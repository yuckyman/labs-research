# Publication Tracking Scripts

This directory contains Python scripts for automated publication tracking.

## Scripts

### `parse-faculty.py`

Parses all `faculty.md` files from lab directories and extracts faculty information.

**Usage:**
```bash
python3 parse-faculty.py > faculty_list.json
```

**Output:** JSON file with faculty names, ORCID IDs, lab associations, and metadata.

**Draft Support:**
- Files with `draft: true` in YAML frontmatter are skipped entirely
- Individual entries with `**Draft:** true` are skipped
- Template entries (like `[Faculty Name]`) are automatically skipped

### `process-publications.py`

Main orchestration script that:
- Queries Crossref, arXiv, and bioRxiv APIs for publications
- Downloads PDFs when available
- Converts PDFs to markdown
- Creates individual publication files

**Usage:**
```bash
python3 process-publications.py faculty_list.json [unpaywall_email]
```

**Dependencies:** Requires `parse-faculty.py` output and calls other scripts.

### `download-pdf.py`

Downloads PDFs from various sources:
- arXiv (direct download)
- bioRxiv (direct download)
- Open access sources via Unpaywall API

**Usage:**
```bash
python3 download-pdf.py <publication_json> [unpaywall_email]
```

**Input:** JSON file with publication metadata
**Output:** JSON with download status and file path

### `pdf-to-markdown.py`

Converts PDF files to Markdown format.

**Usage:**
```bash
python3 pdf-to-markdown.py <pdf_path> [output_path]
```

**Methods tried (in order):**
1. Pandoc (best quality)
2. pdfplumber (good for academic papers)
3. PyPDF2 (fallback)

### `create-publication-file.py`

Creates individual markdown files with YAML frontmatter for each publication.

**Usage:**
```bash
python3 create-publication-file.py <publication_json>
```

**Input:** JSON file with publication data
**Output:** Markdown file in `{lab-name}/publications/{title-slug}.md`

## Dependencies

Install dependencies with:
```bash
pip install -r requirements.txt
```

Required packages:
- `requests` - HTTP requests for APIs
- `PyPDF2` - PDF parsing (fallback)
- `pdfplumber` - PDF parsing (preferred)

System dependencies (installed in workflow):
- `pandoc` - PDF to markdown conversion
- `jq` - JSON parsing
- `libxml2-utils` - XML parsing (xmllint)

## Workflow

The scripts are designed to work together in this order:

1. `parse-faculty.py` → Extract faculty from markdown files
2. `process-publications.py` → Orchestrates the entire process:
   - Queries APIs for each faculty member
   - Calls `download-pdf.py` for each publication
   - Calls `pdf-to-markdown.py` for downloaded PDFs
   - Calls `create-publication-file.py` to create markdown files

## Error Handling

All scripts include error handling and will:
- Continue processing if individual publications fail
- Log errors to stderr
- Return JSON status information
- Respect API rate limits

## Rate Limiting

Scripts include delays between API calls to respect rate limits:
- Crossref: 1 second delay
- arXiv: 1 second delay
- Unpaywall: 1 second delay

## File Structure

Publications are created in:
```
{lab-name}/publications/{title-slug}.md
{lab-name}/publications/{title-slug}.pdf
```

Where `{lab-name}` is the lab directory slug and `{title-slug}` is derived from the publication title.

