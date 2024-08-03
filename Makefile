# Makefile
install: # deps install
        poetry install

lint: #project linter check
        poetry run flake8 brain_games

build: # Build project
        poetry build

publish: # Publish package
        poetry publish --dry-run

package-install: # Install package
        python3 -m pip install --user dist/*.whl

gendiff: # Run project
        poetry run gendiff
