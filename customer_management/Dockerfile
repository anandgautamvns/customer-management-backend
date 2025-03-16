# Use an official Python runtime as a base image.
FROM python:3.12.6

# Prevent Python from writing .pyc files and buffering stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory.
WORKDIR /customer_management

# Copy only requirements to take advantage of Docker cache.
COPY requirements.txt /customer_management/

# Install dependencies.
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code.
COPY . /customer_management/

# Expose the port that your app runs on.
EXPOSE 8000

# Run migrations, optionally collect static files, and start the app using gunicorn.
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn customer_management.wsgi:application --bind 0.0.0.0:8000"]
