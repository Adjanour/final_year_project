%---------------------------------------------------------------
% PhDthesis - Generic Thesis Template
% Based on CUEDthesis by Harish Bhanderi
%---------------------------------------------------------------

\ProvidesClass{Latex/Classes/PhDthesisPSnPDF}[2024 Thesis Class]

% Book class
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions\relax
\ifx\pdfoutput\undefined
   \LoadClass[dvips, a4paper]{book}
\else
   \LoadClass[pdftex, a4paper]{book}
\fi

% Packages
\usepackage{amssymb}
\usepackage{graphics}
\usepackage[margin=12pt,font=small,labelfont=bf]{caption}
\usepackage{eucal}
\usepackage[english]{babel}
\usepackage[usenames, dvipsnames]{color}
\usepackage[perpage]{footmisc}
\usepackage[round, sort, numbers]{natbib}
\usepackage{ifthen}
\usepackage{multicol}
\usepackage[nottoc]{tocbibind}
\usepackage[intoc]{nomencl}
\usepackage{ifpdf}
\usepackage{titletoc}
\usepackage{geometry}
\usepackage{titlesec}
\usepackage{setspace} % For 1.5 spacing

% Glossary
\makenomenclature

% TOC formatting - UMaT standard
\titlecontents{chapter}[0pt]{\bfseries}{\MakeUppercase{\bfseries\chaptername}\ \bfseries\thecontentslabel\quad}{}{\bfseries\hfill\contentspage}

% PDF/Hyperref
\ifpdf
    \usepackage[ pdftex, plainpages = false, pdfpagelabels,
                 bookmarks, bookmarksopen = true, bookmarksnumbered = true,
                 breaklinks = true, linktocpage, pagebackref,
                 colorlinks = false, linkcolor = blue, urlcolor = blue,
                 citecolor = red, anchorcolor = green,
                 hyperindex = true, hyperfigures]{hyperref}
    \DeclareGraphicsExtensions{.png, .jpg, .jpeg, .pdf}
    \usepackage[pdftex]{graphicx}
    \graphicspath{{frontmatter/figures/}}
    \pdfcompresslevel=9
\else
    \usepackage[ dvips, bookmarks, bookmarksopen = true, bookmarksnumbered = true,
                 breaklinks = true, linktocpage, pagebackref,
                 colorlinks = true, linkcolor = blue, urlcolor = blue,
                 citecolor = red, anchorcolor = green,
                 hyperindex = true, hyperfigures]{hyperref}
    \DeclareGraphicsExtensions{.eps, .ps}
    \usepackage{graphicx}
    \graphicspath{{frontmatter/figures/}}
\fi

% Page layout
\ifpdf
    \pdfpageheight=297mm
    \pdfpagewidth=210mm
\else
    \setlength{\paperheight}{297mm}
    \setlength{\paperwidth}{210mm}
\fi
\setlength{\hoffset}{0.00cm}
\setlength{\voffset}{0.00cm}

% Page numbering (UMaT standard: plain, centered in footer)
\pagestyle{plain}

% Chapter heading - UMaT standard (14pt number, 12pt title, centered)
\def\@makechapterhead#1{%
    {\parindent \z@ \centering \normalfont
        \ifnum \c@secnumdepth >\m@ne
            \fontsize{14}{16}\bfseries \MakeUppercase\@chapapp\ \MakeUppercase\thechapter
            \par\nobreak\vskip 10\p@
        \fi
        \fontsize{12}{14}\bfseries #1\par\nobreak
        \vskip 10\p@ }}

% Section headings
\def\section{\@startsection {section}{1}{\z@}%
    {-3.25ex\@plus -1ex \@minus -.2ex}%
    {1.5ex \@plus .2ex}%
    {\normalfont\fontsize{12}{14}\bfseries}}

\def\subsection{\@startsection{subsection}{2}{\z@}%
    {-3.25ex\@plus -1ex \@minus -.2ex}%
    {1.5ex \@plus .2ex}%
    {\normalfont\fontsize{12}{14}\bfseries}}

% Title page commands
\newcommand{\submittedtext}[1]{\gdef\@submittedtext{#1}}
\newcommand{\supervisor}[1]{\gdef\@supervisor{#1}}
\newcommand{\location}[1]{\gdef\@location{#1}}
\newcommand{\faculty}[1]{\gdef\@faculty{#1}}

% Declarations
\def\degreedate#1{\gdef\@degreedate{#1}}
\def\degree#1{\gdef\@degree{#1}}
\def\collegeordept#1{\gdef\@collegeordept{#1}}
\def\university#1{\gdef\@university{#1}}
\def\crest#1{\gdef\@crest{#1}}
\def\title#1{\gdef\@title{#1}}
\def\author#1{\gdef\@author{#1}}

% Default values
\submittedtext{Submitted in Partial Fulfillment}
\supervisor{Supervisor Name}
\location{Tarkwa}
\faculty{Faculty Name}

% Single column environment
\newenvironment{alwayssingle}{%
    \@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
    \else\newpage\fi}%
    {\if@restonecol\twocolumn\else\newpage\fi}

% Title page - UMaT format
\def\maketitl{%
\begin{alwayssingle}
    \thispagestyle{empty}
    \begin{center}
        \vspace{-3cm}
        {\MakeUppercase\@university}\\[0.3cm]
        TARKWA\\[1.0cm]
        % {\@crest}\\[0.3cm]
        {\MakeUppercase\@faculty}\\[0.3cm]
        {\MakeUppercase\@collegeordept}\\[1.5cm]
        {\MakeUppercase\@submittedtext}\\[0.5cm]
        {\bfseries\LARGE\@title}\\[1cm]
        BY\\[\baselineskip]
        {\MakeUppercase\@author}\\[1.5cm]
        SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENT FOR THE\\[0.2cm]
        AWARD OF THE DEGREE OF {\MakeUppercase\@degree}\\[1.5cm]
        PROJECT SUPERVISOR\\[\baselineskip]

        .....................................................

        {\@supervisor}\\[1cm]
        {\MakeUppercase\@location}, GHANA\\[0.5cm]
        {\@degreedate}
    \end{center}
\end{alwayssingle}}

% Front matter environments
\newenvironment{dedication}%
    {\begin{alwayssingle}\pagestyle{plain}\begin{center}\vspace{1cm}\end{center}\begin{quotation}\itshape}%
    {\end{quotation}\end{alwayssingle}}

\newenvironment{acknowledgements}%
    {\begin{alwayssingle}\pagestyle{plain}\begin{center}\vspace{1cm}{\Large\bfseries ACKNOWLEDGEMENTS}\end{center}\vspace{0.5cm}\begin{quotation}}%
    {\end{quotation}\end{alwayssingle}}

\newenvironment{acknowledgementslong}%
    {\begin{alwayssingle}\pagestyle{plain}\begin{center}\vspace{1cm}{\Large\bfseries Acknowledgements}\end{center}\vspace{0.5cm}\begin{quotation}}%
    {\end{quotation}\end{alwayssingle}}

\newenvironment{abstracts}%
    {\begin{alwayssingle}\pagestyle{plain}\begin{center}\vspace{1cm}{\Large\bfseries ABSTRACT}\end{center}\vspace{0.5cm}\begin{quotation}}%
    {\end{quotation}\end{alwayssingle}}

\newenvironment{abstratctslong}%
    {\begin{alwayssingle}\pagestyle{empty}\begin{center}\vspace{1.5cm}{\Large\bfseries Abstract}\end{center}\vspace{0.5cm}\begin{quotation}}%
    {\end{quotation}\end{alwayssingle}}

\newenvironment{abstratctseparate}%
    {\begin{alwayssingle}\pagestyle{empty}\vspace*{-1in}\begin{center}%
    {\Large\bfseries\@title}\par\@author\par\@collegeordept\par\@university\par\@submittedtext\par\@degree\par\@degreedate\end{center}\end{alwayssingle}}%

\newenvironment{declaration}%
    {\begin{alwayssingle}\pagestyle{empty}\begin{center}\vspace{1cm}{\Large\bfseries DECLARATION}\end{center}\vspace{0.5cm}\begin{quotation}}%
    {\end{quotation}\end{alwayssingle}}

\newenvironment{coverpage}%
    {\begin{alwayssingle}\pagestyle{empty}}{\end{alwayssingle}}
