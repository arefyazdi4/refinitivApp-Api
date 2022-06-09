# RefinitivApp Api
an API to represent fetched ESG scores to clients

Tech stacks of this project:
* Django / Djago Rest Framework
* Docker


### 1.  Download the project:

* `git clone "https://github.com/arefyazdi4/refinitivApp-Api"`


### 2. Install Dependencies : 
* python 3.9  
* Django 3.2  
* djangorestframework 3.1   
* django-filter 21.1
      
      
     
## app is not dockerized yet
### 3.  Running the project:
* `python manage.py migrate `  
* `python manage.py seed_db   `
* `python manage.py createsuperuser   `
* `python manage.py runserver  `

## 4.  Now you can see Browsable Api
* Api to see the companies List and Detail -> `127.0.0.1:8000/api/`
* Admin Panel -> `127.0.0.1:8000/admin/`