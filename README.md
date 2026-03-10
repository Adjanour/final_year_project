# UMaT LaTeX Templates

Reusable University of Mines and Technology (UMaT), Tarkwa templates for:

- BSc thesis writing
- BSc defense presentation slides

The templates are already set up with UMaT formatting (title page style, Harvard references, margins, and chapter structure), while keeping placeholders so you can add your own content quickly.

## Repository Layout

```text
.
├── thesis/
│   ├── thesis.tex                    # Main thesis template (use this)
│   ├── example_thesis.tex            # Optional full example layout
│   ├── frontmatter/                  # Abstract, dedication, acknowledgement, logo
│   ├── introduction/                 # Chapter 1
│   ├── literature_review/            # Chapter 2
│   ├── methodology/                  # Chapter 3
│   ├── results_discussion/           # Chapter 4
│   ├── conclusion/                   # Chapter 5
│   ├── backmatter/                   # References + declaration
│   └── Latex/                        # Class/style/bib support files
└── slides/
    ├── defense_template.tex          # Main defense slide template
    ├── references.bib                # Slide references file
    └── figures/                      # Slide images and UMaT logo
```

## Quick Start

### Thesis

```bash
cd thesis
latexmk -pdf thesis.tex
```

Edit these first:

- `thesis/thesis.tex` (title, author, supervisor, degree, date)
- `thesis/frontmatter/*.tex`
- chapter files in `thesis/introduction/` to `thesis/conclusion/`

### Slides

```bash
cd slides
pdflatex defense_template.tex
```

Edit:

- `slides/defense_template.tex` (title block + placeholders)
- `slides/references.bib` (if using citations)

## Notes

- Generated files (`*.aux`, `*.log`, `*.pdf`, etc.) are git-ignored.
- Keep your logo in:
  - `thesis/frontmatter/figures/logo.png`
  - `slides/figures/umatlogo.png`

## Credits

This template is adapted from the work of **Enock Seth Nyamador**:

[https://github.com/enockseth/umat](https://github.com/enockseth/umat)


