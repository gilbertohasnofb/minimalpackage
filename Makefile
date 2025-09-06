.PHONY: setup test format lint

setup:
	@python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt

test:
	@. .venv/bin/activate && python3 -m pytest

format:
	@. .venv/bin/activate && python3 -m black -l 100 .

lint:
	@. .venv/bin/activate && python3 -m black -l 100 . --check