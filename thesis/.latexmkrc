$pdf_mode = 1;
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$bibtex = 'bibtex %O %B';
$max_repeat = 5;
$out_dir = '.';
$aux_dir = '.';

# Keep common generated files removable via latexmk -c/-C.
$clean_ext = 'acn acr alg glg glo gls ist xdy nav snm vrb run.xml synctex.gz brf';
