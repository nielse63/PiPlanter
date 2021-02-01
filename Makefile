files = pyplanter test *.py

setup:
	.bin/setup

install:
	( \
		source .venv/bin/activate; \
		pip install --upgrade pip; \
		pip install -r requirements.txt; \
		pip install -r requirements-dev.txt; \
	)

lint:
	( \
		source .venv/bin/activate; \
		isort $(files); \
		black $(files); \
		flake8 $(files); \
		mypy pyplanter; \
	)

test:
	.bin/test

build:
	make lint
	.bin/build

publish:
	make build
	twine upload --config-file ~/.pypirc -r pypi dist/*

docs:
	rm -rf docts/dest
	sphinx-build docs/_src docs/dest -c docs

.PHONY: test build
