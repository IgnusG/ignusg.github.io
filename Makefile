pygment:
	pygmentize -S $(target) -f html > assets/css/highlight.css

watch:
	bundle exec jekyll serve --watch
