
# Django Chalçenge 001
This is the reposiroty of the challenge

## What was developed
I never used Django Rest Framework before, so i couldn't complete all the challenge. The main reason was the difficulty with django's erros. The language is not dificult to understand, but how I had a deadline, I cant study some features enough

## Endpoints
 - http://localhost:8000/api/articles/ CRUD
 - http://localhost:8000/api/authors/ CRUD
 - http://localhost:8000/api/sign-up/ Its not working as I wanted

## 🗒 To run

1. Clone the repository

   - `git@github.com:pedrohrbispo/djangoChallenge.git`.
   - Go to repository folder you just cloned:
     - `cd djangoChallenge`

2. Make sure you have installed djando-admin, python, python3, postgresql, and runing a venv:

3. Change in the settings.py file the credentials of your database:
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}

4. run python manage.py makemigrations

5. run python manage.py migrate

6. run python manage.py runserver
  - the server will run on port 8000

