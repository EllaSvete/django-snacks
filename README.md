# Lab 26

## Django Snacks

### Author

- Ella Svete

### Setup

- python3 -m venv .venv
- source .venv/bin/activate
- pip install django
- django-admin startproject snack_tracker_project
- python manage.py migrate
- python manage.py runserver
- python manage.py startapp snacks
- Make TUV and add to settings

### Tests

- declare class SnacksTests that extends SimpleTestCase
- import django.test import SimpleTestCase
- python manage.py test to run tests

- I referenced the tests provided in today's demo
