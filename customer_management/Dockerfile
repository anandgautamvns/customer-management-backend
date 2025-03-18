# Use an official Python runtime as a parent image
FROM python:3.12.6

# Prevents Python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures stdout and stderr are sent straight to terminal (e.g. your container log)
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies (including PostgreSQL client libraries)
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Copy and install requirements
# COPY requirements.txt /app/
COPY customer_management/requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files into the container
COPY . /app/

# Expose port 8000 (adjust if needed)
EXPOSE 8000

# Run Django migrations and start the application using Gunicorn
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn customer_management.wsgi:application --bind 0.0.0.0:8000"]