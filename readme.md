This project is named "Hoori" which refers to the japanese god Hoori who was the god of grain and rice. The reason for this is that the site will collect recipes and to give give a helping hand in the style direction of the user interface, that will aim to be sleek and minimalistic. 

**TO DO**

**Django Project**

1. install django and libraries
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


**SETUP DATABASE MODEL**

1. models.py
- add imports
- Use our database scheme
- enter the items into models.py
- makemigrations then migrate 
2. 

**SETUP RECIPES(POSTS)**
- summernote
