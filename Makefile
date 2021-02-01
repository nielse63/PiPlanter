src = piplanter test
files = $(src) *.py

setup:
	.bin/setup

install:
	( \
		source path/to/virtualenv/bin/activate; \
		pip install --upgrade pip \
		pip install -r requirements.txt \
		pip install -r requirements-dev.txt
	)

lint:
	( \
		source path/to/virtualenv/bin/activate; \
		black piplanter test \
		flake8 piplanter test \
		mypy piplanter
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
