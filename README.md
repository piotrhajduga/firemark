# Firemark - web based rpg/adventure/riddle game

Browser riddle game empowering it's players to create new locations/levels
through a relatively simple interface. The inspiration was an expandable
adventure/riddle game. However the possibilities are far bigger.

## Nerd talk ahead in this section ;)

Right now after years of experimentations it settled on Django. The main reason
is the development speed. The aim is, after estabilishing the ERD for the
database to use as much already available components and libraries as possible.

The author hopes he can create something usable until he gets bored... again.

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
