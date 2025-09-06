.PHONY: setup  black_format black_check flake8 pydocstyle isort unit_tests

FLAKE_IGNORE = E203,E266,W503
FLAKE_EXCLUDE = .venv,./sandbox.py
PYDOCSTYLE_SELECT = D101,D102,D103,D105,D107,D300,D301

setup:
	@python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt

black_format:
	@. .venv/bin/activate && python3 -m black -l 100 .

black_check:
	@. .venv/bin/activate && python3 -m black -l 100 . --check

flake8:
	@. .venv/bin/activate && python3 -m flake8 --ignore=${FLAKE_IGNORE} --exclude=${FLAKE_EXCLUDE}

pydocstyle:
	@. .venv/bin/activate && python3 -m pydocstyle --select=${PYDOCSTYLE_SELECT}
	
isort:
	@. .venv/bin/activate && python3 -m isort --check-only --diff --line-length=100 --multi-line=3 --project=minimalpackage --skip=sandbox.py --skip-gitignore  --trailing-comma --use-parentheses .

unit_tests:
	@. .venv/bin/activate && python3 -m pytest