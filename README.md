# refinitivApp-Api
an API to represent fetched ESG scores to clients

dependencies :  
Django 3.2  
djangorestframework 3.1   
django-filter 21.1    
drf-nested-routers 0.93



app is not dockerized yet so after you clone it and installed dependencies run following commands:

python manage.py migrate   
python manage.py seed_db   
python manage.py createsuperuser   
python manage.py runserver  

