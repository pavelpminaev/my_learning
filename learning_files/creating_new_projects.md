# create new poetry directory
$ poetry new project_name

# install dependens of project
$ poetry install

# add new dependens (packeges) in project
$ poetry add --group dev pytest prompt poetry wemake-python-styleguide

# make git-repo
$ git init -b main
$ git add . && git commit -m 'innitial commit'
$ gh repo create  # choose > Push an existing local repo..

Зарегистрируйтесь на CodeClimate (при регистрации выбирайте ветку Quality)
Подключите к нему свой репозиторий
Разместите в ридми бейджик Maintainability своего проекта (см. https://docs.codeclimate.com/docs/overview#badges)


