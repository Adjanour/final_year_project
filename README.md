# UMaT Project Report — LaTeX Template

A structured LaTeX template for undergraduate project reports at the
**University of Mines and Technology, Tarkwa (UMaT)**, based on the
MastersDoctoralThesis v1.6 class (LaTeXTemplates.com), adapted for the
Faculty of Computing and Mathematical Sciences format.

---

## Prerequisites

| Tool | Install |
| --- | --- |
| TeX Live (full) | `sudo pacman -S texlive` · `sudo apt install texlive-full` |
| latexmk | Included in TeX Live |
| BibTeX | Included in TeX Live |

VS Code extension (**optional but recommended**): [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)

---

## Quick Start

```bash
# One-time or full rebuild (cleans first)
latexmk -C thesis.tex && latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -recorder thesis.tex

# Incremental rebuild (only re-runs what changed)
latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -recorder thesis.tex

# Continuous watch mode (auto-rebuild on save)
latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -recorder -pvc thesis.tex
```

Output: **`thesis.pdf`**

Intermediate files (`.aux`, `.log`, `.bbl`, etc.) are kept during normal builds
for faster incremental compiles and reliable SyncTeX. Use clean tasks/commands
from [docs/building.md](docs/building.md) when needed.

---

## Project Structure

```text
thesis.tex              Root driver — document class + \include list only
preamble.tex            All packages, formatting, and thesis metadata
references.bib          Bibliography database (BibTeX format)
TemplateClassFile.cls   Document class (do not edit)

FrontMatter/
  titlepage.tex         Title page
  declaration.tex       Authorship declaration (all group members)
  abstract.tex          Abstract  ← replace \lipsum with real text
  dedication.tex        Dedication
  acknowledgements.tex  Acknowledgements
  lists.tex             Table of Contents, LoF, LoT, Abbreviations

Chapters/
  Chapter1.tex          Introduction
  Chapter2.tex          …
  Chapter6.tex          Conclusion

Appendices/
  AppendixA.tex         Appendix A  (uncomment in thesis.tex when ready)
  AppendixB.tex         Appendix B

Figures/                Place all images here (.pdf, .png, .jpg)

docs/                   Extended documentation
  building.md           Build system, cleanup, troubleshooting
  structure.md          File-by-file reference
  customisation.md      How to add chapters, figures, citations, etc.

.latexmkrc              latexmk configuration (auto-cleanup, PDF mode)
.vscode/tasks.json      VS Code build tasks
```

---

## VS Code Tasks

Open the Command Palette → **Tasks: Run Task**

| Task | Action |
| --- | --- |
| **Build PDF (latexmk)** | Incremental build → `thesis.pdf` |
| **Clean Aux (latexmk -c)** | Remove aux files, keep `thesis.pdf` |
| **Clean + Build PDF (latexmk)** | Full clean rebuild → `thesis.pdf` |
| **Watch PDF (latexmk -pvc)** | Auto-rebuild continuously while editing |

---

## Further Reading

- [Building & the build system](docs/building.md)
- [File structure reference](docs/structure.md)
- [Customising the report](docs/customisation.md)
