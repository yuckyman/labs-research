# Labs Research Tracker

A comprehensive tracking system for research laboratories, faculty members, and publications in computational neuroscience and cognitive science.

## Purpose

This repository serves as a centralized knowledge base for tracking:
- Research laboratories and their focus areas
- Faculty members and their research interests
- Publications and academic output
- Emerging research trends and collaborations

## Automated Publication Tracking

This repository includes **automated publication tracking** via GitHub Actions that:
- 🔍 Queries Crossref, arXiv, and bioRxiv APIs for publications
- 📥 Downloads full-text PDFs when available (arXiv, bioRxiv, open access)
- 📄 Converts PDFs to markdown for machine readability
- 📝 Creates individual publication files with YAML frontmatter
- 🔗 Integrates seamlessly with Obsidian Bases

**The system is fully modular** - each lab directory is processed independently, making it easy to add new labs or configure existing ones.

## Structure

### Lab Directories (Modular Design)

Each lab has its own directory containing:
- `lab.md` - Laboratory overview and contact information
- `faculty.md` - **Faculty roster with research profiles** (required for automated tracking)
- `publications.md` - Publication tracking table (legacy, now auto-generated)
- `publications/` - **Auto-generated directory** containing:
  - Individual markdown files for each publication (`{title-slug}.md`)
  - PDF files when available (`{title-slug}.pdf`)

### Tracking
The `tracking/` directory contains:
- Research trend observations
- Cross-lab collaboration notes
- Literature review summaries

## Current Labs

- **Berlin BCCN** - Bernstein Center for Computational Neuroscience
- **Berlin School** - Berlin School of Mind and Brain
- **Copenhagen** - University of Copenhagen
- **Karolinska** - Karolinska Institute (Stockholm)
- **Max Planck Frankfurt** - Max Planck Institute for Brain Research
- **Max Planck Tübingen** - Max Planck Institute for Biological Cybernetics
- **MPII** - Max Planck Institute for Intelligent Systems
- **Neuro-Interaction Innovation Lab** - Kennesaw State University
- **Radboud University** - Donders Institute for Brain, Cognition and Behaviour
- **Tübingen University** - University of Tübingen
- **UCL** - University College London

## Configuring Lab Folders for GitHub Actions

To maximize compatibility with the automated publication tracking system, follow these guidelines when setting up or updating lab folders:

### Required: `faculty.md` Format

The GitHub Actions workflow automatically parses `faculty.md` files from each lab directory. To ensure proper tracking:

1. **Use YAML frontmatter (optional but recommended):**
   ```markdown
   ---
   tags: [faculty, lab-name]
   type: faculty-list
   draft: false  # Set to true to skip entire file
   ---
   ```
   - **`draft: true`** - Skips the entire file (useful for template files)
   - **`draft: false`** or omitted - File will be processed
   - This prevents processing template files with placeholder entries

2. **Use the correct heading format:**
   ```markdown
   ### Faculty Name
   ```
   - Each faculty member must be under a `###` heading
   - Use the actual name (not `[Faculty Name]` or template placeholders)

3. **Include metadata fields:**
   ```markdown
   ### John-Dylan Haynes
   
   **Position:** Professor, Theory & Analysis of Brain Signals
   **Email:** [email@institution.de]
   **Website:** https://example.com
   **ORCID:** 0000-0000-0000-0000
   ```
   - **ORCID** (highly recommended): Enables more accurate publication matching
   - **Email**: Optional, for contact info
   - **Website**: Optional, for linking
   - **Position**: Optional, for context

4. **Mark individual entries as drafts (optional):**
   ```markdown
   ### Person 1
   
   **Draft:** true
   **Position:** [To be updated]
   ```
   - Add `**Draft:** true` to skip individual faculty entries
   - Useful when you have placeholder entries mixed with real ones

5. **Avoid template placeholders:**
   - ❌ `[Faculty Name]` - Won't be processed (automatically skipped)
   - ❌ `[To be updated]` - Won't be processed (automatically skipped)
   - ❌ `[ORCID ID]` - Won't be processed (automatically skipped)
   - ✅ Use actual names and data
   - ✅ Or mark as draft if you need placeholders

6. **Example valid entry:**
   ```markdown
   ---
   tags: [faculty, radboud-university]
   type: faculty-list
   draft: false
   ---
   
   # Faculty - Radboud University
   
   ### Floris de Lange
   
   **Position:** Professor of Perception & Cognition
   **Email:** floris.delange@donders.ru.nl
   **Website:** https://www.ru.nl/en/people/de-lange-f
   **ORCID:** 0000-0002-7291-4758
   
   **Research Interests:**
   - Predictive processing
   - Perception and decision-making
   ```

7. **Example draft file (skipped entirely):**
   ```markdown
   ---
   tags: [faculty, lab-name]
   type: faculty-list
   draft: true
   ---
   
   # Faculty - Lab Name
   
   ### [Faculty Name]
   
   **Position:** [To be updated]
   ```

### Lab Directory Naming

- Use lowercase with hyphens: `max-planck-tubingen`, `radboud-university`
- Avoid spaces and special characters
- Directory name becomes the `lab_slug` used in publication files

### Adding a New Lab

1. Create a new directory: `{lab-name}/`
2. Add `lab.md` with lab overview
3. Add `faculty.md` with faculty members (see format above)
4. Add `publications.md` (optional, legacy format)
5. The `publications/` directory will be auto-created by the workflow

### Modularity Benefits

- **Independent Processing**: Each lab is processed separately - failures in one lab don't affect others
- **Easy Addition**: Just add a new directory with `faculty.md` - no workflow changes needed
- **Flexible Configuration**: Each lab can have different faculty structures
- **Automatic Discovery**: The workflow finds all lab directories automatically

## Usage with Obsidian

This repository is optimized for use with [Obsidian](https://obsidian.md/):
- Internal links use `[[]]` syntax
- Tags for categorization
- YAML frontmatter for metadata
- **Obsidian Bases integration** - See [OBSIDIAN_BASES_SETUP.md](OBSIDIAN_BASES_SETUP.md) for detailed setup

### Quick Start with Obsidian Bases

1. Enable the Bases core plugin in Obsidian
2. Create a base in any `publications/` folder
3. Filter and view publications by lab, faculty, year, or fulltext availability
4. See [OBSIDIAN_BASES_SETUP.md](OBSIDIAN_BASES_SETUP.md) for complete guide

## GitHub Actions Workflow

The publication tracking workflow (`track-publications.yml`) runs:
- **Automatically**: Every Monday at 9 AM UTC
- **Manually**: Via GitHub Actions tab → "Run workflow"

### What It Does

1. Parses all `faculty.md` files from lab directories
2. Queries Crossref, arXiv, and bioRxiv for each faculty member
3. Downloads PDFs from open access sources (arXiv, bioRxiv, Unpaywall)
4. Converts PDFs to markdown
5. Creates individual publication files with YAML frontmatter
6. Commits and pushes new publications

### Configuration

- **Unpaywall Email** (optional): Set `UNPAYWALL_EMAIL` secret in GitHub for better open access detection
- **Rate Limiting**: Built-in delays respect API rate limits
- **Error Handling**: Continues processing even if individual publications fail

See [.github/IMPLEMENTATION_SUMMARY.md](.github/IMPLEMENTATION_SUMMARY.md) for technical details.

## Contributing

When adding new labs or updating information:

1. **Follow the existing template structure**
2. **Use proper `faculty.md` format** (see above) for automated tracking
3. **Maintain consistent formatting**
4. **Include all relevant links and contact information**
5. **Add ORCID IDs** when available (improves publication matching)
6. **Update this README** with new lab entries

### Best Practices

- ✅ Use actual faculty names (not templates)
- ✅ Include ORCID IDs for better matching
- ✅ Keep directory names lowercase with hyphens
- ✅ Use consistent markdown formatting
- ✅ Link to faculty websites and profiles
- ✅ Mark template files as `draft: true` in frontmatter to skip them
- ✅ Use `**Draft:** true` for individual placeholder entries

---

## Documentation

- **[OBSIDIAN_BASES_SETUP.md](OBSIDIAN_BASES_SETUP.md)** - Complete guide for using Obsidian Bases
- **[.github/IMPLEMENTATION_SUMMARY.md](.github/IMPLEMENTATION_SUMMARY.md)** - Technical implementation details
- **[.github/scripts/README.md](.github/scripts/README.md)** - Script documentation

---

*Last updated: November 2025*