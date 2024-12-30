# Use the official Python 3.9-slim image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Expose port 8000 for the Django application
EXPOSE 8000

# Set the default command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
