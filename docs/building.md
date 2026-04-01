# Building the Report

## Tools

The build system uses **latexmk**, which orchestrates pdflatex and BibTeX,
re-running them the correct number of times to resolve cross-references and
citations automatically.

Configuration lives in [`.latexmkrc`](../.latexmkrc) at the project root.

---

## Everyday Build Commands

```bash
# Incremental build — only re-runs what changed (fastest)
latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -recorder thesis.tex

# Full clean rebuild — always starts from scratch
latexmk -C thesis.tex && latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -recorder thesis.tex

# Continuous watch mode (auto-rebuild on save)
latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -recorder -pvc thesis.tex

# Wipe ALL generated files including thesis.pdf
latexmk -C thesis.tex
```

### VS Code Tasks (shortcut)

Open the Command Palette (`Ctrl+Shift+P`) → **Tasks: Run Task**:

| Task | Equivalent command |
| --- | --- |
| Build PDF (latexmk) | `latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -recorder thesis.tex` |
| Clean Aux (latexmk -c) | `latexmk -c thesis.tex` |
| Clean + Build PDF (latexmk) | `latexmk -C thesis.tex && latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -recorder thesis.tex` |
| Watch PDF (latexmk -pvc) | `latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -recorder -pvc thesis.tex` |

---

## Automatic Cleanup

Use the clean tasks/commands when you want to remove generated files:

- `latexmk -c thesis.tex` keeps `thesis.pdf` and removes aux files.
- `latexmk -C thesis.tex` removes aux files and `thesis.pdf`.

This keeps SyncTeX files available during normal editing and watch mode.

---

## How Many Passes Run

latexmk runs pdflatex and BibTeX as many times as needed (up to `$max_repeat = 10`):

1. **pdflatex** — produces initial `.aux` with citation keys
2. **bibtex** — reads `references.bib`, writes `.bbl`
3. **pdflatex** × 2–3 — resolves references, page numbers, ToC

A typical clean build runs pdflatex 3–4 times. Incremental builds run only
what changed.

---

## Troubleshooting

### "I found no \citation commands" / 0 bibliography entries

The `.aux` file was empty when BibTeX ran, meaning pdflatex exited early with
a hard error. Check the `.log` file:

```bash
latexmk -pdf thesis.tex; cat thesis.log | grep -i error
```

Common causes: a missing `\usepackage`, an undefined command, or a syntax error.

### Citations appear as `[?]` or `(Author?, Year?)`

Run a **Clean + Build** to force all passes from scratch:

```bash
latexmk -C && latexmk -pdf thesis.tex
```

### Package not found

Install the missing TeX Live package:

```bash
# Arch Linux
sudo pacman -S texlive-latex  # or texlive-latexextra, texlive-science, etc.

# Ubuntu / Debian
sudo apt install texlive-latex-extra
```

Or install individual packages with `tlmgr`:

```bash
tlmgr install <package-name>
```

### latexmk reports "Nothing to do" but PDF is stale

Force a rebuild by touching the source:

```bash
touch thesis.tex && latexmk -pdf thesis.tex
```
