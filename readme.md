**hoori.**


This project is named "Hoori" which refers to the japanese god Hoori who was the god of grain and rice. The reason for this is that the site will collect recipes and to give give a helping hand in the style direction of the user interface, that will aim to be sleek and minimalistic. 

add progrsm to rquirements after install
pip3 freeze --local > requirements.txt

**Logotype**
The logo is based on the "Helvetica" font in bold, all lowercaps letters with a dot in the end in an attempt to keep the logo sleek and easy. 

**Design**
**Theme**
White background with black lettering to achieve a minimalistic look and have high contrast in order for the page to have good useability. Will use th e color crimson red which is the red color on japans flag. Its a distinc red that will give the website a splash of color. Also, gold will be used as a nod to grain since hoori is the god of grain and rice. 

**Header**
The header will be white and black and will be a key point for the user in their navigation and interaction with the site as the header will  be dynamic in regards to the status of the visitor (logged in or not). When the user is logged in they should be presented with the option to sign out and view their own recipes. 

**body**
The body will handle the displa for the recipes. 
**footer** 
Social links as well as copyright information. 

**icons**
ICons used will relate to "hoori" thus we will use icons depicting grains, rice, cooking and utensils.
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
- python3 manage.py makemigrations
- python3 manage.py migrate
2. Run migrations each time we wish make changes that efffect databases such as changes in settings and models.py

**SETUP RECIPES(POSTS)**
- summernote
- added autoamtic slugs
- added possiblity to comment
- added filters for admin
- 

**new view**
1. create the view code
2. create a template to render view
3. connect URLS in urls.py


**Crispy Forms**
1. install crispy forms
2. 

