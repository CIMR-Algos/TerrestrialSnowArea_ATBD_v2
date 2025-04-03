all:
	jupyter-book build --all .

pdf:
	jupyter-book build --all . --builder pdflatex

gh-pages:
	ghp-import -n -p -f _build/html

clean:
	rm -rf ./_build
