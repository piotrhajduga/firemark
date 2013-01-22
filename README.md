# Firemark - web based rpg/adventure/riddle game

## Contents of the repository

* **/py2.7** - virtualenv configured to run the project

* **/static** - directory containing all the static content for the website
    * **/static/js** - javascripts
    * **/static/img** - images
    * **/static/css** - css stylesheets
    * **/static/misc** - miscellanous static content

* **/templates** - page templates written using Mako

* **/bricks** - directory containing bricks - building blocks of every location

* **/actions** - python package with controllers for specific urls

* **/engine** - utilities used by controllers

* **/tests** - tests invoked from the root directory using trial, e.g.:    
    ```$ trial tests.engine.user```

## Dependencies

* **SQLAlchemy** 0.8.0b2

* **Mako** 0.7.3

* **Twisted Web** 12.1.0
