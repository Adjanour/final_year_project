$do_cd = 1;
$out_dir = '.';
$aux_dir = '.';
$pdf_mode = 1;

$pdflatex = 'pdflatex -interaction=nonstopmode -file-line-error -synctex=1 -recorder %O %S';
$bibtex = 'bibtex %O %B';
$pdf_previewer = 'sioyek --reuse-window --inverse-search "code -g \"%1\":%2" %O %S';

$max_repeat = 5;
$clean_ext = 'bbl synctex.gz %R-blx.bib run.xml';
