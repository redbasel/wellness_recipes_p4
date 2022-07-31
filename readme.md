## hoori.

**table of contents**

## Table of contents
1. [Introduction](#Introduction)
2. [Start](#Start)
3. [Functionality](#Functionality)
    1. [User Stories](#User-Stories)
    2. [Issues](#Issues)
    3. [Functionality: Design](#Functionality:-Design)
4. [Design](#Design)
    1. [Wireframes](#Wireframes)
    2. [Database](#Database)
    3. [Fonts](#Fonts)
    4. [Logotype](#Logotypes)
    5. [Icons](#Icons) 

5. [Issues](#Issues)
6. [Testing](#Testing)
    1. [Validators](#Validators)
    2. [User Stories](#User-story-testing)
    3. [Feature Testing](#Feature-tests)
    4. [Bugs](#Bugs)

7. [Technologies](#Technologies)
8. [Deployment](#Deployment)
8. [Credit](#Credit)







## Introduction

This project is named "Hoori" which refers to the japanese god Hoori who was the god of grain and rice. The reason for this is that the site will collect recipes with the intent to break them down to their core which is the reason that the macros are included. Further, it will give a helping hand in the style direction of the user interface, that will aim to be sleek and minimalistic. 

Link to the live project:

https://hoori-recipes.herokuapp.com/

![Introduction](/static/media/homeimg.png 'home ')

## Start

## Functionality

### User Stories



https://github.com/redbasel/wellness_recipes_p4/issues?q=is%3Aissue+is%3Aopen+label%3A%22User+story%22

### Wireframes


### Functionality: Design

## Design

### Wireframes

The original wireframe for the navbar desktop view.


![Design](/static/media/WebNavBarwf.png 'wireframe navbar')

Wireframe of the hoomepage as a visitor.

![Design](/static/media/Webvisitorwf.png 'wireframe visitor')

Wireframe of the homepage as a logged in user

![Design](/static/media/webloggedinwf.png 'wireframe logged in user homepage')

Wireframes of the recipe section of the website.



![Design](/static/media/Recipe_detail.png 'Recipe detail1 wireframe')

![Design](/static/media/Recipe_detail_new%20%E2%80%93%201.png 'REcipe detail2 wireframe ')

### Database scheme

Below is the database scheme for the application. 

![Design](/static/media/database_scheme.png 'database scheme')

### Fonts

The two most featured fonts on the website are Helvetica and IBM Plex Mono. The helvetiva is used for the logo and the items in the header along with the hero text as well as the title of the recipes. The monotype font "IBM Plex Mono" was used to give the site a more minimalistic design as well as giving the feeling that the recipes are more intiamte as they have bee nwritte non a tyypewriter almost by someones grandma couple decades back. The design takes cues from the "nothing. brand".  

### Colortheme

The name hoori is of japanese origin and relates to wheat, thus there are four main colors on the page. Namely, white, red, gold and black. The white and red comes from the japanese flag, adn the page is using the offical red of the japanese flag "Crimson Glory". The gold is a nod to the wheat and the "golden" harvest. The black ties it all together. The image used for the hero have elements of theses colors as well. 


![Design](/static/media/colors2.png 'color scheme')

### Logotype

The logo is based on the "Helvetica" font in bold, all lowercaps letters with a dot in the end in an attempt to keep the logo sleek and easy. 

![Design](/static/media/hoorilogo.png 'hoori logotype')

### Icons

Upgraded FontAwesome to the latest version 6.1.2 from 5.15.4 in order to be able to utilize the wheat icon. 



## Issues

https://github.com/redbasel/wellness_recipes_p4/issues?q=is%3Aissue+is%3Aopen+label%3Aissue

## Testing

Below is a summary of the tesing done.


### Validators

#### html - w3c

Gave some warnings but  nothing detrimental as it reacted a lot on the django references, 

#### css - jigsaw

![validator](/static/media/cssvalidator.png 'css')


#### python - PEP8


Utilized the built in PEP8 validator in Gitpod to go through the python files and made the changes i could that did not effect the function of the webpage, it was mostly cleaning up the code. There is a warning for aline of code that is too long in models.py but it could not be amended without the page becoming unstable. 


#### lighthouse 

Homepage:

Desktop scored a 95 and on mobile it scored a 74 overall. To increase this score the two improvements aside from ascesiblilty would be to have smaller images that would load on the mobile decies as well as implementing lazy load on the recipes. Improvments could be made to create a alt field that the user can fill in or have the title of the recipe fill in the alt of the images to increase accesiblit. This would apply to both desktop and mobile.


![validator](/static/media/lighthomedesk.png 'lightdeskp')

![validator](/static/media/lighthomemobile.png 'lighttmobile')


Recipe page:

On desktop the recipe page scored a 100 overall. Improvements could be made to assesibility. On mobile it scored a 97. 

![validator](/static/media/lightrecipedesk.png 'lightdeskrecipe')

![validator](/static/media/lightrecipemobile.png 'lightmobilerecipe')




### User story testing

Write my user stories and how they are adresssed.

USER STORY: Users add image to recipe form 

![User story testing](/static/media/imgupload.png 'Upload image - testing')

USER STORY: Enter detailed 'instructions' recipe form     

![User story testing](/static/media/detailed_input_1.png 'detailed instructions - testing')

USER STORY: Only owner can delete post     

Only the owner will be shown the delete and edit buttons as shown below. If the user tries to acess the edit or delete page by pasting the correct url directly into the browser there is a second check that first checks if the user is authenticated and secondly if they are the author. If they are not the the author they will directed to a error page and if they are not logged in they will be asked to please log in. 

![User story testing](/static/media/user_delete.png 'author can delete - testing') 

![User story testing](/static/media/defensive_delete.png 'defensive programming - testing')

![User story testing](/static/media/unauth_delete.png 'visitor can not delete - testing')

![User story testing](/static/media/notauthorized.png 'direct entry denied not auth - testing')

![User story testing](/static/media/please_log_in.png 'direct entry denied login - testing')

USER STORY: Alerts      

When signed in the site will send out an alert to confirm thay you have been logged in. The site will also send out a alert when you are succesfully logged out. 

![User story testing](/static/media/signin_alert.png 'alert signin - testing')

![User story testing](/static/media/signout_alert.png 'alert signout - testing')


USER STORY: comment on recipes     

Logged in users should be able to comment on all posts and when the comment is made it should be sent to the admin for approval. When approved it should show under the post and and comment counter should increase by one.

![User story testing](/static/media/commentbox.png 'commentbox - testing')

![User story testing](/static/media/admin_approve.png 'admin approve - testing')

![User story testing](/static/media/commentapproved.png 'comment approved - testing')



USER STORY: view post list      



USER STORY: website pagination      

USER STORY: Create posts      

A logged in user should be able to upload recipes. When logged in the user will be promted to upload a recipe in the header.

![User story testing](/static/media/header:change.png 'CRUD upload navbara - testing')

![User story testing](/static/media/upload_recipe.png 'CRUD upload - testing')

USER STORY: VIEW OWN RECIPES   

To be implemented at a later date. 

USER STORY: Display recipes on page      

USER STORY: EDIT RECIPE 

Only the owner will be shown the delete and edit buttons as shown below. If the user tries to acess the edit or delete page by pasting the correct url directly into the browser there is a second check that first checks if the user is authenticated and secondly if they are the author. If they are not the the author they will directed to a error page and if they are not logged in they will be asked to please log in. 

![User story testing](/static/media/detailed_input.png 'update recipe - testing')

![User story testing](/static/media/unauth_delete.png 'visitor can not delete - testing')

![User story testing](/static/media/notauthorized.png 'direct entry denied not auth - testing')

![User story testing](/static/media/please_log_in.png 'direct entry denied login - testing')

USER STORY: View recipe     

Users can view recipe by hovering over the recipe, and when they do that the text will change to gold to indicate it can be clicked to the user. 

![User story testing](/static/media/view_recipe.png 'users can view recipes - testing')


USER STORY: Like recipe      

Users can like a recipe and when doing so the like counter should increae by one on bothe the recipe page but also in the recipe list. 

![User story testing](/static/media/recipepost_notliked.png 'recipe post not liked - testing')

![User story testing](/static/media/recipepost_liked.png 'recipe post liked - testing')

![User story testing](/static/media/recipe_liked.png 'recipe liked - testing')
  

USER STORY: Log in     

Visitors should be able to login to their accounts. 

![User story testing](/static/media/navbarlogin.png 'navbar login - testing')

![User story testing](/static/media/signin.png 'signin page - testing')



USER STORY: Register account  

A visitor should be able to register a account and will be encouraged to do som in the the hero and will have acess to the register link in the navbar.

![User story testing](/static/media/navbar_register.png 'navbar register - testing')

![User story testing](/static/media/hero_signup.png 'navbar signup - testing')




### Feature tests

Check that all buttons and links works and act as intended to. 

#### Navbar

The navbar has a couple of buttons and properties which need to be tested that they direct the user to the correct place but also that they shift property based on the status of the user i.e if they are a visitor or logged in user. 

##### As a visitor

"home" when pressed should take you to the starting page. 

"register" when pressed should take you to the signup page.

"login" when pressed should take you to the sign in page.

The user "status" should say "user:visitor" when not logged in.


##### As a logged in user

"home" when pressed should take you to the starting page. 

"register" should have changed to "logout" and when pressed should take you to the "signout" page, asking if you are sure.

"log in" should have changed to "add a recipe" and when pressed should take you to the "add recipe" form where you will fill out all details regarding the recipe. 

The user "status" should say "user:'username'" when not logged in. 'username' is a placeholder for the name of the logged in user. 

#### Homepage

The hero has variable elements based on whether the visitor is a logged in user or just a visitor.

##### Hero as a logged in user

When logged in the hero text should firstly, welcome the user and secondly the button should act as “Create Recipe” button. 

As a visitor the hero text should inform the users about the possible features of the website and enquire them to sign up.


#### Homepage: recipe list

The visitor/user should be able to see rows of recipes, and the recipes are displayed using cards. The user should see a banner above the recipe image with a quick and concsice summmary of the macros, "p" for protein, "c" for carbs and "f" for fats. Below the image and flash is where the title of the recipe should be. Below that should the author of the recipe be found along with the amount of likes that should be syymbolized by a wheat of grain alongside a likes counter. When you hover over the title it should turn gold. 

#### Homepage: Footer

The footer should contain socials and a quote regarding the origin of hoori. 


### Bugs

https://github.com/redbasel/wellness_recipes_p4/issues?q=is%3Aissue+is%3Aopen+label%3Aissue



### Improvements

The webiste is functional today and working, however as with all projects there is room for improvement which the following list summarizes:

1. Add a rich text editor on the user end, not just for admin. One of the problems of the rich text editors on the user end is the danger of injection attacks which makes it a bigger taask than just simply allowing it on teh user end. Sutiable editors would be SummerNote, TinyMCE and CKeditor. 
2. Adding tags so that users could filter out recipes based on their dietary preferences.
3. Adding a social share button could increase the amount of recipes being shared amongst friends and this increasing the userbase.


## Deployment

First, add all dependencies to requirements.txt using: pip3 freeze > requirements.txt. Secondly, push and commit to git. That’s for git, and for Heroku we create a new app. Add the name and venture on to the settings before deployment. Add our cred file with our private api key. In buildpacks we add python and node.js, in that order. That’s it for the settings, back to deployment. We connect our github account, search for the repo. Then manually deploy the branch so we are in full control.


## Tecnologies

### Languages

Language used involved:
1. Python
2. HTML
3. Javascript
4. CSS

## Credits

Credits go to CodeInstitute and the "I think therefore I blog" whcih served as an inspiration for the project. 
