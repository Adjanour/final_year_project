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
latexmk -pdf thesis.tex

# Full clean rebuild — always starts from scratch
latexmk -C && latexmk -pdf thesis.tex

# Wipe ALL generated files including thesis.pdf
latexmk -C
```

### VS Code Tasks (shortcut)

Open the Command Palette (`Ctrl+Shift+P`) → **Tasks: Run Task**:

| Task | Equivalent command |
|---|---|
| Build PDF (latexmk) | `latexmk -pdf thesis.tex` |
| Clean + Build PDF (latexmk) | `latexmk -C && latexmk -pdf thesis.tex` |

---

## Automatic Cleanup

After every **successful** build, latexmk automatically deletes all
intermediate files, leaving only the source and `thesis.pdf`.

This is configured in `.latexmkrc` via:

```perl
$success_cmd = 'latexmk -c %S && rm -f %R.bbl';
$clean_ext   = 'bbl synctex.gz %R-blx.bib run.xml';
```

Files removed: `.aux`, `.log`, `.toc`, `.lof`, `.lot`, `.out`, `.fls`,
`.fdb_latexmk`, `.bbl`, `.blg`, `.synctex.gz`, `-blx.bib`, `.run.xml`

`thesis.pdf` is **always kept**.

> **Note:** The `.synctex.gz` file (used for PDF ↔ source sync in editors) is
> also removed. If you need it, remove `synctex.gz` from `$clean_ext` in
> `.latexmkrc`.

---

## How Many Passes Run

latexmk runs pdflatex and BibTeX as many times as needed (up to `$max_repeat = 5`):

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
