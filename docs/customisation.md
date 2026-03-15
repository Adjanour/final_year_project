# Customising the Report

Practical instructions for the most common editing tasks.

---

## Thesis Metadata

Open **`preamble.tex`** and fill in the `Thesis Metadata` section near the
bottom of the file:

```latex
\thesistitle{Your Full Project Title}          % printed with \ttitle
\author{Your Name in Full}                     % printed with \authorname
\supervisor{Dr Eric Affum}                     % printed with \supname
\university{University of Mines and Technology, Tarkwa}  % \univname
\department{Department of Computer Science and Engineering}  % \deptname
\faculty{Faculty of Computing and Mathematical Sciences}   % \facname
\degree{Bachelor of Science in Computer Science and Engineering}  % \degreename

% Location and date on the title page
\renewcommand{\submissionplace}{Tarkwa, Ghana}
\renewcommand{\submissiondate}{May, 2026}
```

These values are also embedded in the PDF metadata automatically.
`FrontMatter/titlepage.tex` uses them directly — **do not edit the title page file itself**.

---

## Title Page

Edit **`FrontMatter/titlepage.tex`**.  
Replace the placeholder lines for the project title, your names, supervisor
name, and the submission date.

---

## Declaration

Edit **`FrontMatter/declaration.tex`**.  
Update the student names and index numbers in the declaration body and in the
four signature lines.

---

## Abstract

Edit **`FrontMatter/abstract.tex`**.  
Replace `\lipsum[2-3]` with the real abstract text (no `\lipsum` import will be
needed once done — you can also remove `\usepackage{lipsum}` from `preamble.tex`).

---

## Adding / Renaming Chapters

1. Create a new file in `Chapters/`, e.g. `Chapter7.tex`.
2. Start the file with:

   ```latex
   \chapter{Your Chapter Title}
   \label{ch:your-label}
   ```

3. Add an `\include` line to `thesis.tex` in the `Main Chapters` section:

   ```latex
   \include{Chapters/Chapter7}
   ```

Chapters are included **in the order they appear** in `thesis.tex`.

---

## Adding a Section / Subsection

Inside any chapter file, use the standard LaTeX heading commands:

```latex
\section{Section Title}
\subsection{Subsection Title}
\subsubsection{Subsubsection Title}
```

---

## Adding Figures

1. Copy the image file into `Figures/`.
2. In your chapter:

   ```latex
   \begin{figure}[H]
     \centering
     \includegraphics[width=0.8\linewidth]{my-diagram.pdf}
     \caption{A descriptive caption.}
     \label{fig:my-diagram}
   \end{figure}
   ```

3. Reference it in text: `Figure~\ref{fig:my-diagram}`.

> Use `.pdf` or `.eps` for vector graphics (diagrams, plots) and `.png`/`.jpg`
> for raster images (screenshots, photos). Vector formats scale cleanly at any size.

---

## Adding Tables

```latex
\begin{table}[H]
  \centering
  \caption{Table caption goes above the table.}
  \label{tab:my-table}
  \begin{tabular}{lcc}
    \hline
    \tabhead{Column A} & \tabhead{Column B} & \tabhead{Column C} \\
    \hline
    Row 1 & value & value \\
    Row 2 & value & value \\
    \hline
  \end{tabular}
\end{table}
```

Reference: `Table~\ref{tab:my-table}`.

---

## Adding Bibliography Entries

Open **`references.bib`** and add a BibTeX entry. Common types:

```bibtex
@article{lastname2024keyword,
  author  = {Last, First and Other, Author},
  title   = {Paper Title},
  journal = {Journal Name},
  year    = {2024},
  volume  = {12},
  pages   = {100--110},
}

@inproceedings{lastname2024conf,
  author    = {Last, First},
  title     = {Paper Title},
  booktitle = {Proceedings of the Conference},
  year      = {2024},
  pages     = {50--58},
}

@misc{org2024report,
  author = {{Organisation Name}},   % double braces = treat as single name
  title  = {Report Title},
  year   = {2024},
  url    = {https://example.com},
}
```

Cite in text:

```latex
\citep{lastname2024keyword}      % (Author, 2024)
\citet{lastname2024keyword}      % Author (2024)
\citep[p.~5]{lastname2024keyword} % (Author, 2024, p. 5)
```

After adding new entries, run a **Clean + Build** to let BibTeX pick them up.

---

## Adding Abbreviations

Open **`FrontMatter/lists.tex`** and add rows to the `abbreviations` table:

```latex
\begin{abbreviations}{lr}
  \textbf{CNN}  & \hspace{3cm}\qquad Convolutional Neural Network \\
  \textbf{LSTM} & \hspace{3cm}\qquad Long Short-Term Memory \\
\end{abbreviations}
```

Entries appear in the order listed — sort alphabetically before submission.

---

## Enabling Appendices

In **`thesis.tex`**, uncomment the `\include` lines in the Appendices section:

```latex
\appendix
\include{Appendices/AppendixA}
\include{Appendices/AppendixB}
```

Each appendix file should start with `\chapter{Appendix Title}`.

---

## Changing Page Margins

In **`preamble.tex`**, edit the `geometry` line:

```latex
\usepackage[a4paper, top=1in, bottom=1in, left=1.2in, right=1in, head=21.75pt]{geometry}
```

> Keep `head=21.75pt` — removing it causes a `scrlayer-scrpage` warning about
> the running header being too large.

---

## Changing Line Spacing

In **`preamble.tex`**, the `\linespread` command controls body text spacing.
The document class also accepts `onehalfspacing` or `doublespacing` as class
options in `thesis.tex`, but `\linespread{1.5}` in the preamble takes precedence.

```latex
\linespread{1.0}   % single
\linespread{1.5}   % 1.5× (current default)
\linespread{2.0}   % double
```
