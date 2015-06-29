# Firemark - web based rpg/adventure/riddle game

From Ground-Up

## Running

1. Initialize virtualenv

    mkvirtualenv firemark-django -ppython3

2. Enable virtualenv

    workon firemark-django

3. Install python dependencies through pip

    pip install -r firemark_django/requirements.txt

4. Migrate database

    cd firemark_django/
    python manage.py migrate

### Development server

    cd firemark_django/
    python manage.py runserver
