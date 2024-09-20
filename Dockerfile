# Use the official Python image from Docker Hub
FROM python:3.12

# Set the working directory in the container to the Django project folder
WORKDIR /django_interview_project

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire django_interview_project directory to the container
COPY django_interview_project/ .

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

