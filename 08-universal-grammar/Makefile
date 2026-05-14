PAPER = universal_grammar
LATEX = pdflatex
LATEXOPTS = -interaction=nonstopmode -halt-on-error

.PHONY: all clean view

all: $(PAPER).pdf

$(PAPER).pdf: $(PAPER).tex
	$(LATEX) $(LATEXOPTS) $(PAPER).tex
	$(LATEX) $(LATEXOPTS) $(PAPER).tex
	$(LATEX) $(LATEXOPTS) $(PAPER).tex

view: $(PAPER).pdf
	open $(PAPER).pdf

clean:
	rm -f $(PAPER).aux $(PAPER).log $(PAPER).out $(PAPER).toc

distclean: clean
	rm -f $(PAPER).pdf
