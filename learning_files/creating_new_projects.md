Create new poetry directory
```bash
poetry new project_name
```
Install dependens of project
```bash
poetry install
```
Add new dependens (packeges) in project
```bash
poetry add --group dev pytest prompt
```
Add linter
```bash
poetry add --group dev wemake-python-styleguide
```
```bash
poetry add --group dev black
```


```bash
poetry add --group dev mypy # static type checker for Python.
```

 - isort

 - pre-commit


add setup.cfg - file configuration
``````
[coverage:run]
branch = True

[flake8]
accept-encodings = utf-8
max-complexity = 6
statistics = False
max-line-length = 80
doctests = True
enable-extensions = G
isort-show-traceback = True

# clean default ignore list
ignore =

per-file-ignores =
  # it is possibble to have prints in scripts
  packege/subpackege/*.py: WPS421

[tool:pytest]
norecursedirs = __pycache__
addopts = --strict-markers

[isort]
# See https://github.com/timothycrosley/isort#multi-line-output-modes
multi_line_output = 3
include_trailing_comma = true
default_section = FIRSTPARTY
# Should be: 80 - 1
line_length = 79
``````


Make git-repo
```bash
git init -b main
```
```bash
git add . && git commit -m 'innitial commit'
```
Create and choose 'Push an existing local repo..'
```bash
gh repo create
```
> Зарегистрируйтесь на CodeClimate (при регистрации выбирайте ветку Quality)
> Подключите к нему свой репозиторий
> Разместите в ридми бейджик Maintainability своего проекта (см. https://docs.codeclimate.com/docs/overview#badges)

- Create Makefile

Добавьте в Makefile команду build, которая выполнит 
```bash
poetry build
```
Добавьте в Makefile команду publish, которая выполнит
```bash
poetry publish --dry-run
````
Добавьте в Makefile команду package-install, которая выполнит 
```bash
python3 -m pip install --user dist/*.whl
```
Добавьте в Makefile команду 'clean' for experiments
```
clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml
```


Добавьте в .toml
>[tool.poetry.scripts]\
brain-games = "package_name.scripts.module:main"'

example for markdown file:
``` python3
# It`s python code

def function():
    return result
```
