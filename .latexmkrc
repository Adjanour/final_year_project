$do_cd = 1;
$out_dir = '.';
$aux_dir = '.';
$pdf_mode = 1;

$pdflatex = 'pdflatex -interaction=nonstopmode -file-line-error -synctex=1 -recorder %O %S';
$bibtex = 'bibtex %O %B';

$max_repeat = 5;
$clean_ext = 'bbl synctex.gz %R-blx.bib run.xml';

# After every successful build, remove intermediate files automatically.
# %S = source file (e.g. thesis.tex)  %R = root base name (e.g. thesis)
$success_cmd = 'latexmk -c %S && rm -f %R.bbl';
