**Customer Management Backend(Python-Django)**
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

**Prerequisites**
  Python 3.8 or later
  pip
  virtualenv (optional, Python includes venv in the standard library)
  Docker (for containerized deployment)

**Getting Started**
**1. Clone the Repository**
  git clone https://github.com/anandgautamvns/customer-management-backend.git
  cd Customer-management-backend

**2. Create a Virtual Environment**
  **Create a virtual environment to isolate your project's dependencies:**

Windows:
  python -m venv env
  .\env\Scripts\activate

macOS/Linux:
  python3 -m venv env
  source env/bin/activate

**3. Install Dependencies**
**Install Django and other dependencies:**
  pip install -r requirements.txt
  Note: To add additional packages, install them via pip and update requirements.txt with:
  pip freeze > requirements.txt

**4. Database Setup**
  Make migrations and update your database:
  python manage.py makemigrations
  python manage.py migrate

  **Create a superuser for accessing the Django admin:**
    python manage.py createsuperuser

**5. Running the Development Server**
  Start the Django development server:
  python manage.py runserver
  Visit http://localhost:8000 in your browser to see the application running.

**6. Deleting the Database (Optional)**
If you need to reset your database:

  macOS/Linux:
  rm db.sqlite3

  Windows:
  del db.sqlite3

**Docker Deployment**
This project is containerized using Docker and Docker Compose.

**Dockerfile**
The Dockerfile sets up a lightweight Python environment, installs system and Python dependencies, and runs the Django application using Gunicorn.

**docker-compose.yml**
The docker-compose.yml file configures two services: one for the Django application and one for PostgreSQL (or your preferred database).

Build and Run Containers
Build and run the containers with:
  docker-compose up --build
  After the build completes, your application should be accessible at http://localhost:8000.

Additional Information
Settings Configuration:
Adjust your Django settings (e.g., DEBUG, ALLOWED_HOSTS, and database configuration) in customer_management/settings.py to suit your production environment.

Static Files:
Configure static files handling (e.g., using WhiteNoise) if deploying to production.

**Testing:**
  Run your tests with:
  python manage.py test

