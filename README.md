# Firemark - web based rpg/adventure/riddle game

## Contents of the repository

* **/static** - directory containing all the static content for the website
    * **/static/desktop** - desktop page static files
        * **/static/desktop/js** - javascripts
        * **/static/desktop/img** - images
        * **/static/desktop/css** - css stylesheets
    * **/static/common** - common static files

* **/templates** - page templates written using Mako
    * **/templates/desktop** - desktop page templates

* **/actions** - python package with controllers
    * **/actions/json** - JSON API controllers (package)
    * **/actions/desktop** - desktop page controllers (package)

* **/engine** - utilities used by controllers

* **/tests** - tests invoked using trial, e.g.: `$ trial tests`

## Dependencies

* **SQLAlchemy** 0.8.0b2

* **Mako** 0.7.3

* **Twisted Web** 12.1.0

## Running

For now if all dependencies are met development app server can be started by
getting into virtual environment and running `$ ./run.py`

And everything should go smoothly.
Report any issues on a
[bugtracker at Bitbucket](https://bitbucket.org/kosarock/firemark/issues)

