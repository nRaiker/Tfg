#!/bin/bash

pdflatex   proyecto.tex
pdflatex   proyecto.tex

rm {*.aux,*.lof,*.log,*.lol,*.lot,*.out,*.synctex.gz,*toc}
