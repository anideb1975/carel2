# Django Carel2 Project


## Installation and Run

- Create Virtual environment
  - python -m venv env
  - source ./env/bin/activate
  - pip install -r core/requirements.txt
- Create database
  - cd core
  - python manage.py makemigrations
  - python manage.py migrate

- Create superuser
  - python manage.py createsuperuser

* Run the application
  - python manage.py runserver

