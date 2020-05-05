pygment:
	pygmentize -S $(target) -f html > assets/css/highlight.css

watch:
	bundle exec jekyll serve --watch

resize_post_images:
	python ./resize-post-images.py
	git add assets/img/posts
