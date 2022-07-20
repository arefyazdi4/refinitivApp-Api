# RefinitivApp Api
an API to represent fetched ESG scores to clients

Tech stacks of this project:
* Django / Djago Rest Framework
* Docker
* redis
* celery 
* JWT
* Pytest as a test tool


### 1.  Download the project:

* `git clone "https://github.com/arefyazdi4/refinitivApp-Api"`


### 2.  Build The Project:

* `docker-compose build`

### 3.  Running the project:

* `docker-compose up ` \ `docker-compose up -d`
      

### 4.  Setting up the project:
* `docker exec -it refinitivApp sh`
* `python manage.py migrate `  
* `python manage.py seed_db   `
* `python manage.py createsuperuser   `


## 5.  Now you can see Browsable Api
* Api to see the companies List and Detail -> `127.0.0.1:8000/api/`
* Admin Panel -> `127.0.0.1:8000/admin/`
* Api to JWT authentication -> `127.0.0.1:8000/auth/jwt/create/`