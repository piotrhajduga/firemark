# Firemark - web based rpg/adventure/riddle game

## Contents of the repository

* **/webapp** - directory containing all the static content for the website
    * **/webapp/desktop** - desktop page static files
        * **/webapp/desktop/js** - javascripts
        * **/webapp/desktop/img** - images
        * **/webapp/desktop/css** - css stylesheets
    * **/webapp/common** - common static files

* **/templates** - page templates written using Mako
    * **/templates/desktop** - desktop page templates

* **/actions** - python package with controllers
    * **/actions/json** - JSON API controllers (package)
    * **/actions/desktop** - desktop page controllers (package)

* **/engine** - utilities used by controllers

* **/tests** - unittests

## Dependencies

For virtualenv requirements consult requirements.txt in the project's root
directory.

## Running

### Development server

For now if all dependencies are met development app server can be started by
getting into virtual environment and running `$ ./run.py`

And everything should go smoothly.

### Tests

To run all the tests just run `$ nosetests`

## Issues

Report any issues on a
[bugtracker at Bitbucket](https://bitbucket.org/kosarock/firemark/issues)

