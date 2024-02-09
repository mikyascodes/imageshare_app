This is a Django project where users can create account and post pictures. the users can see all the pictures posted by all the users on a imagepage.  They can also see the image they shared on their profile page.
To run the project run the following commands:
1. *** To create virtual enviroment ***
- pip install virtualenv
- virtualenv env
- env\Scripts\activate.bat
2. *** Install python packge ***
- pip install -r requirements.txt
3. *** For the database ***
- cd imageshare_app
- python manage.py makemigrations
- python manage.py migrate
4. *** To create superuser ***
- python manage.py createsuperuser
5. *** Finally runserver ***
- python manage.py runserver


