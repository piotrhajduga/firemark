# Firemark - web based rpg/adventure/riddle game

From Ground-Up

## Running

Initialize virtualenv

    mkvirtualenv firemark-django -ppython3

Enable virtualenv

    workon firemark-django

Install python dependencies through pip

    pip install -r firemark_django/requirements.txt

Migrate database

    cd firemark_django/
    python manage.py migrate

### Development server

    cd firemark_django/
    python manage.py runserver
