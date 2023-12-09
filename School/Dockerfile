# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Install sqlite3
RUN apt-get update && apt-get install -y sqlite3

# Copy the requirements folder into the container at /app/requirements
COPY requirement/development.txt /app/requirements/development.txt

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements/development.txt


# Copy the content of the local src directory to the working directory
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run on container start
CMD ["python", "School/manage.py", "runserver", "0.0.0.0:8000"]

