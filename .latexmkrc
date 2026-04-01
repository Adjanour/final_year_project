$do_cd = 1;
$out_dir = '.';
$aux_dir = '.';
$pdf_mode = 1;
$recorder = 1;
$synctex = 1;
$bibtex_use = 2;

$pdflatex = 'pdflatex -interaction=nonstopmode -file-line-error -synctex=1 -recorder %O %S';
$lualatex = 'lualatex -interaction=nonstopmode -file-line-error -synctex=1 -recorder %O %S';
$xelatex = 'xelatex -interaction=nonstopmode -file-line-error -synctex=1 -recorder %O %S';
$bibtex = 'bibtex %O %B';
$pdf_previewer = 'sioyek --reuse-window --inverse-search "code -g \"%1\":%2" %O %S';

$max_repeat = 10;

add_cus_dep('glo', 'gls', 0, 'run_makeglossaries');
add_cus_dep('acn', 'acr', 0, 'run_makeglossaries');
sub run_makeglossaries {
	if ($silent) {
		system "makeglossaries -q $_[0]";
	} else {
		system "makeglossaries $_[0]";
	}
}

push @generated_exts, 'glo', 'gls', 'glg', 'acn', 'acr', 'alg';
$clean_ext .= ' %R-blx.bib %R.run.xml %R.bcf %R.glo %R.gls %R.glg %R.acn %R.acr %R.alg %R.ist %R.xdy synctex.gz';
