# Use an official Python runtime as a base image.
FROM python:3.9-slim

# Prevent Python from writing .pyc files and buffering stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory.
WORKDIR /app

# Copy only requirements to take advantage of Docker cache.
COPY requirements.txt /app/

# Install dependencies.
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code.
COPY . /app/

# Expose the port that your app runs on.
EXPOSE 8000

# Run migrations and start the app using gunicorn.
CMD python manage.py migrate && gunicorn customer_management.wsgi:application --bind 0.0.0.0:8000