**table of contents**

## Table of contents
1. [Introduction](#Introduction)
2. [Start](#Start)


using following commands:
- pip3 install 'django<4' gunicorn
- pip3 install dj_database_url psycopg2
- pip3 install dj3-cloudinary-storage
2. create new, blank django project and app
- pip3 freeze --local > requirements.txt
- django-admin startproject [name_of_folder_to_be_created] .
- python3 manage.py startapp [name_of_new_app]
(after adding hoori_recipes to apps in settings then we migrate)
- python3 manage.py migrate

(Heroku setup)
- Crete new project
- add-on postgres as our database.  
- edit env.py and settings file.

3. set project to use Cloudinary and PostgreSQL
4. Deploy empty project to Heroku. 
- Create procfile and add folliwing web: gunicorn hoori.wsgi (hoori is name of folder for startproject)

## Start

using following commands:
- pip3 install 'django<4' gunicorn
- pip3 install dj_database_url psycopg2
- pip3 install dj3-cloudinary-storage
2. create new, blank django project and app
- pip3 freeze --local > requirements.txt
- django-admin startproject [name_of_folder_to_be_created] .
- python3 manage.py startapp [name_of_new_app]
(after adding hoori_recipes to apps in settings then we migrate)
- python3 manage.py migrate

(Heroku setup)
- Crete new project
- add-on postgres as our database.  
- edit env.py and settings file.

3. set project to use Cloudinary and PostgreSQL
4. Deploy empty project to Heroku. 
- Create procfile and add folliwing web: gunicorn hoori.wsgi (hoori is name of folder for startproject)
