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

Добавьте в .toml
>[tool.poetry.scripts]\
brain-games = "package_name.scripts.module:main"'

example for markdown file:
``` python3
# It`s python code

def function():
    return result
```
