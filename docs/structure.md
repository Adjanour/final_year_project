# File Structure Reference

A description of every file and folder in the project, and what to edit where.

---

## Root Files

### `thesis.tex`

The **entry point** for the build. It should contain almost nothing except:

- The `\documentclass[...]{TemplateClassFile}` declaration
- `\input{preamble}`
- `\include{...}` calls for front matter and chapters
- `\printbibliography`

Do **not** put packages or formatting here — those belong in `preamble.tex`.

### `preamble.tex`

All packages, formatting rules, and thesis metadata.
Loaded once by `thesis.tex` via `\input{preamble}`.

Sections inside the file (clearly labelled with `%===` banners):

| Section | What it controls |
|---|---|
| Page Layout | Paper size, margins, header height |
| Font & Encoding | Times New Roman, UTF-8, T1 |
| Abstract Fix | Removes trailing blank page after abstract |
| Bibliography | biblatex/BibTeX settings, citation style, "et al." italics |
| Chapter & Section Headings | Font size, spacing, capitalisation |
| Tables & Figures | graphicx, tabularx, float, longtable, subcaption |
| Mathematics | amsmath |
| Lists | enumitem (for labelled list variants) |
| Typography | microtype, hyphenat |
| ToC / List Formatting | tocloft, etoc, tocbibind, dot leaders, indentation |
| Convenience Commands | `\keyword{}`, `\code{}`, `\file{}`, `\tabhead{}`, `\option{}` |
| Line Spacing & Captions | 1.5× spread, bold label, custom separator |
| Thesis Metadata | Title, author, university, department, etc. |

### `references.bib`

BibTeX bibliography database. Add entries here.
See [customisation.md](customisation.md#adding-bibliography-entries) for details.

### `TemplateClassFile.cls`

The document class. Derived from the MastersDoctoralThesis v1.6 template.
**Do not edit** — it defines the `\thesistitle`, `\author`, front-matter
environments, and page styling that the rest of the project depends on.

### `example.bib`

Unused sample bibliography file from the original template. Safe to delete.

---

## `FrontMatter/`

Each file holds exactly one front-matter section.
All are `\include`d from `thesis.tex` and appear in this order:

| File | Purpose | What to edit |
|---|---|---|
| `titlepage.tex` | Cover page | Project title, supervisor, names, date |
| `declaration.tex` | Authorship declaration | Student names and index numbers |
| `abstract.tex` | Abstract | Replace `\lipsum[2-3]` with real abstract text |
| `dedication.tex` | Dedication | Replace sample dedication text |
| `acknowledgements.tex` | Acknowledgements | Replace sample acknowledgement text |
| `lists.tex` | ToC, LoF, LoT, Abbreviations | Add/remove abbreviation rows |

---

## `Chapters/`

| File | Chapter |
|---|---|
| `Chapter1.tex` | Introduction |
| `Chapter2.tex` | Literature Review (or as assigned) |
| `Chapter3.tex` | Methodology |
| `Chapter4.tex` | Implementation / Results |
| `Chapter5.tex` | Evaluation / Discussion |
| `Chapter6.tex` | Conclusion *(not yet included in thesis.tex — uncomment when ready)* |

Each chapter starts with `\chapter{Title}` and contains `\section`, `\subsection` etc.

---

## `Appendices/`

| File | Contents |
|---|---|
| `AppendixA.tex` | Appendix A (uncomment the `\include` line in `thesis.tex`) |
| `AppendixB.tex` | Appendix B |
| `AppendixTemplate.tex` | Blank template for new appendices |

---

## `Figures/`

Drop all images here (`.pdf`, `.png`, `.jpg`, `.eps`).
The path is set in `preamble.tex`:

```latex
\graphicspath{{Figures/}}
```

So you can reference images without the path prefix:

```latex
\includegraphics[width=\linewidth]{my-diagram.pdf}
```

---

## Config & IDE Files

| File | Purpose |
|---|---|
| `.latexmkrc` | latexmk build config — PDF mode, compiler flags, auto-cleanup |
| `.vscode/tasks.json` | VS Code build tasks |
| `.vscode/settings.json` | VS Code workspace settings |

---

## Build Output

| File | Description | Keep? |
|---|---|---|
| `thesis.pdf` | Final output | **Yes** |
| `*.aux`, `*.log`, `*.bbl`, etc. | Intermediates | Auto-deleted after build |
