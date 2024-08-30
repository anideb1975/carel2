# Django Carel2 Project

## Installation and Run

* Create Virtual environment
  - python -m venv env
  - source ./env/bin/activate
  - pip install -r requirements.txt

* Create database
  - cd core
  - python manage.py makemigrations
  - python manage.py migrate

* Create superuser
  - python manage.py createsuperuser

* Run the application
  - python manage.py runserver

- Access
  - First login only super user ,add account select register in your index page appropriate level for account
  - note application multilevel and multiuser with various role and access

* Database
  - development version use sqlite3
  - you can change database edit settings.py and configure your preferred db example mysql or mariadb

* Production
  - remember run
  - python manage.py collectstatic

