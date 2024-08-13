# Makefile
lint: #project linter check
	poetry run flake8 gendiff

install: # deps install
	poetry install

build: # Build project
	rm -f ./dist/*
	poetry build

publish: # Publish package
	poetry publish --dry-run

package-install: # Install package
	python3 -m pip install --user dist/*.whl

gendiff: # Run project
	poetry run gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
