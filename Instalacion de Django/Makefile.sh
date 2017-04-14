#!/bin/bash

pdflatex -synctex=1 -interaction=nonstopmode  Django.tex
pdflatex -synctex=1 -interaction=nonstopmode  Django.tex

rm {*.aux,*.lof,*.log,*.lol,*.lot,*.out,*.synctex.gz,*toc}