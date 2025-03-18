**Python – Django Microservice**
**Project Structure**
Customer-management-backend/
├── customer_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── customer/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── user/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
├── venv


**Create a virtual environment** 
	python -m venv env
	deactivate (deactivate)
  
**Activate the Virtual Environment**
	.\env\Scripts\activate (Window)
	source env/bin/activate (Mac OS)

**Install Django and all dependency**
	pip install Django
	django-admin startproject myproject (Create Project)
	python manage.py runserver (Run Project)
	pip freeze > requirements.txt (create file)
	pip install -r requirements.txt (Install all dependency)
	python manage.py makemigrations ( Database Create)
	python manager.py migrate  (Database update)
	python manage.py createsuperuser (database user)
  
**Delete Database**
	rm db.sqlite3  (macOS/Linux)
	del db.sqlite3  (Windows)
