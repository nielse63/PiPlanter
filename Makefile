src = pytemplate test
files = $(src) *.py
test_files = *

setup:
	.bin/setup

install:
	.bin/install

lint:
	black pytemplate test
	flake8 pytemplate test
	mypy pytemplate

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
