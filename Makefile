# Define variables
PYTHON = python
PYLINT = pylint
BLACK = black
PYTEST = pytest
DOCKER = docker

# Install dependencies
install:
	pip install --upgrade pip && pip install -r requirements.txt

# Format code using Black
format:
	$(BLACK) *.py

# Lint code using Pylint
lint:
	$(PYLINT) --disable=R,C --ignore-patterns=test_*?py *.py

# Run tests using Pytest
test:
	$(PYTHON) -m pytest --cov=main test_main.py
	
# Default target
all: install format lint test
