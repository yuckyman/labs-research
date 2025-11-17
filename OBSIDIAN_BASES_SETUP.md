# Obsidian Bases Setup Guide

This guide explains how to use Obsidian's Bases plugin to organize and view publications from the automated tracking system.

## Overview

The publication tracking system creates individual markdown files for each publication with YAML frontmatter containing metadata. These files are perfect for use with Obsidian Bases, which allows you to create database-like views of your notes.

## File Structure

Publications are stored in:
```
{lab-name}/publications/{title-slug}.md
```

Each publication file contains:
- YAML frontmatter with metadata (title, authors, year, DOI, etc.)
- Full text content (if PDF was downloaded and converted)
- Abstract (if full text not available)
- Links to DOI, arXiv, bioRxiv, etc.

## Setting Up Bases

### 1. Enable Bases Plugin

1. Open Obsidian Settings (⚙️)
2. Go to "Core plugins"
3. Enable "Bases" (if not already enabled)

### 2. Create a Base for Publications

#### Option A: Create Base via Command Palette

1. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows/Linux)
2. Type "Bases: Create new base"
3. Select a folder (e.g., `max-planck-tubingen/publications`)
4. Name your base (e.g., "Publications")

#### Option B: Create Base via File Explorer

1. Right-click on a publications folder
2. Select "New base"
3. Name your base

### 3. Configure Base Views

After creating a base, you can configure different views:

#### Table View

Shows publications in a table format with columns for:
- Title
- Authors
- Year
- Journal
- DOI
- Lab
- Faculty
- Tags

**To customize columns:**
1. Click the "..." menu in the base view
2. Select "Configure base"
3. Add/remove columns as needed

#### Card View

Displays publications as cards with key information visible.

**To switch to card view:**
1. Click the view selector (usually at the top)
2. Select "Cards"

#### List View

Simple list view showing titles and metadata.

### 4. Filtering Publications

You can filter publications by various criteria:

#### Filter by Lab

```
filters:
  and:
    - file.path.contains("max-planck-tubingen")
```

#### Filter by Faculty Member

```
filters:
  and:
    - file.frontmatter.faculty.contains("John-Dylan Haynes")
```

#### Filter by Year

```
filters:
  and:
    - file.frontmatter.year >= 2024
```

#### Filter by Fulltext Availability

```
filters:
  and:
    - file.frontmatter.fulltext_available = true
```

#### Filter by Source

```
filters:
  and:
    - file.frontmatter.fulltext_source = "arxiv"
```

### 5. Sorting Publications

Sort publications by:
- Year (descending - newest first)
- Title (alphabetical)
- Journal
- Faculty member

**To add sorting:**
1. Open base configuration
2. Add sort rules
3. Specify field and direction (ascending/descending)

### 6. Example Base Configuration

Here's an example base configuration for viewing all publications:

```yaml
filters:
  and:
    - file.hasTag("publication")

views:
  - type: table
    name: "All Publications"
    order:
      - file.frontmatter.year desc
      - file.name asc
    columns:
      - file.name
      - file.frontmatter.title
      - file.frontmatter.authors
      - file.frontmatter.year
      - file.frontmatter.journal
      - file.frontmatter.doi
      - file.frontmatter.lab
      - file.frontmatter.fulltext_available
```

### 7. Creating Lab-Specific Bases

Create a base for each lab to organize publications:

1. Navigate to `{lab-name}/publications/`
2. Create a new base
3. Configure filters to show only publications from that lab
4. Add custom views for that lab's research focus

Example for Max Planck Tübingen:

```yaml
filters:
  and:
    - file.path.contains("max-planck-tubingen/publications")

views:
  - type: table
    name: "MPI Tübingen Publications"
    order:
      - file.frontmatter.year desc
```

### 8. Linking Publications to Faculty

Publications automatically link to faculty members via the `faculty` frontmatter field. To view publications by faculty:

1. Create a base filtered by faculty name
2. Or use the faculty links in each publication file

Example filter for a specific faculty member:

```yaml
filters:
  and:
    - file.frontmatter.faculty.contains("Floris de Lange")
```

### 9. Advanced Queries

You can create more complex queries:

#### Recent Publications (Last 2 Years)

```yaml
filters:
  and:
    - file.frontmatter.year >= 2023
```

#### Open Access Only

```yaml
filters:
  and:
    - file.frontmatter.fulltext_available = true
    - file.frontmatter.fulltext_source != "none"
```

#### Publications with Full Text

```yaml
filters:
  and:
    - file.frontmatter.fulltext_available = true
```

#### Publications Needing PDF Download

```yaml
filters:
  and:
    - file.frontmatter.fulltext_available = false
```

### 10. Embedding Bases in Notes

You can embed a base view in any note:

```
![[publications.base]]
```

To embed a specific view:

```
![[publications.base#All Publications]]
```

### 11. Custom Properties

Each publication file has these properties available in Bases:

- `title` - Publication title
- `authors` - List of authors
- `year` - Publication year
- `journal` - Journal name
- `doi` - DOI identifier
- `arxiv_id` - arXiv ID (if applicable)
- `biorxiv_id` - bioRxiv ID (if applicable)
- `url` - Publication URL
- `pdf_path` - Path to PDF file
- `lab` - Lab slug
- `faculty` - List of faculty members
- `tags` - List of tags
- `abstract` - Abstract (only if fulltext not available)
- `fulltext_available` - Boolean indicating if PDF is available
- `fulltext_source` - Source of fulltext (arxiv, biorxiv, unpaywall, none)
- `created` - Date when file was created

### 12. Tips and Best Practices

1. **Create Multiple Views**: Create different views for different purposes (recent publications, by lab, by faculty, etc.)

2. **Use Tags**: The system automatically adds tags like `publication` and the lab name. You can add custom tags manually.

3. **Link to Faculty Pages**: Each publication links to faculty members. Click these links to see all publications by that faculty member.

4. **Search Within Bases**: Use Obsidian's search within a base to find specific publications.

5. **Export Views**: You can export base views as CSV or other formats for external analysis.

6. **Combine with Other Plugins**: Use Bases with other Obsidian plugins like Dataview for more advanced queries.

## Troubleshooting

### Publications Not Showing Up

- Check that the files are in the correct directory structure
- Verify YAML frontmatter is properly formatted
- Ensure filters match the file structure

### Base Not Updating

- Refresh the base view
- Check that files are being created correctly
- Verify the base configuration matches your file structure

### PDF Links Not Working

- Ensure PDF files are in the correct location
- Check that `pdf_path` in frontmatter matches actual file location
- Verify file permissions

## Example Workflows

### View All Recent Publications

1. Create a base with filter: `year >= 2024`
2. Sort by year descending
3. Use table view with key columns

### Track Publications by Lab

1. Create a base for each lab directory
2. Filter by lab path
3. Customize views per lab's needs

### Find Open Access Papers

1. Create base with filter: `fulltext_available = true`
2. Add column for `fulltext_source`
3. Sort by year to see recent open access papers

## Additional Resources

- [Obsidian Bases Documentation](https://help.obsidian.md/bases)
- [YAML Frontmatter Guide](https://help.obsidian.md/advanced-topics/metadata)
- [Obsidian Community Forums](https://forum.obsidian.md/)

---

*Last updated: November 2025*

