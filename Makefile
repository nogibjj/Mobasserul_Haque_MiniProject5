install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py
	
lint:
	ruff check *.py

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py	

all: install format lint test

generate_and_push:
	# Create the markdown file 
	python test.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add SQL log as query_output.md"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

extract:
	python main.py extract

load: 
	python main.py transform_load	