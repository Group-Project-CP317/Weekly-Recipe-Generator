# Weekly-Recipe-Generator
CP317 Project
#Weekly Recipe Generator

Steps to run the application
1. clone the github repository - git clone https://github.com/Group-Project-CP317/Weekly-Recipe-Generator.git
2. install packages with the command - pip install django, pillow, requests
4. make migration changes - python manage.py makemigrations
5. migrate changes - python manage.py migrate
6. run the server (website will load at (https://127.0.0.1:8000/) - python manage.py runserver

Create an account and add recipes or search for them

To view the login, register, profile, create-recipe:
You can change the web address, like https://127.0.01:8000/login , https://127.0.0.1:8000/register , etc.

Things that are completed:
1. User creation
2. Login/Logout
3. Searching recipes in database
4. viewing recipes in database
5. creating recipes

Things that are not completed:
1. random recipe not implemented - (not possible in the time frame)
2. image upload for recipe
3. recipe favoriting
4. using recipe's from api (we get the response and can parse the data, just needs to be pushed to template)
5. searching recipe's from api
