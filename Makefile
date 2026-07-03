PYTHON := .venv/bin/python

.PHONY: black-check black-reformat clean check  isort-check isort-reformat reformat ruff setup test

# Setup
.venv/.installed: requirements.txt requirements-dev.txt requirements-test.txt
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	.venv/bin/pip install -r requirements-dev.txt
	.venv/bin/pip install -r requirements-test.txt
	touch .venv/.installed
setup: .venv/.installed

# Formatting and linting
black-check:
	@$(PYTHON) -m black --check --diff .
black-reformat:
	@$(PYTHON) -m black .
isort-check:
	@$(PYTHON) -m isort --check-only --diff .
ruff:
	@$(PYTHON) -m ruff check .
check: black-check  isort-check ruff
reformat: black-reformat isort-reformat

# Unit testing
test:
	@$(PYTHON) -m pytest

# Cleanup
clean:
	find . -type f -name "*.pyc" -delete && find . -type d -name "__pycache__" -delete