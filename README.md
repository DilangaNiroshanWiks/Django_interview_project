# Django Interview Project

## Description
A Django project to visualize assessment data using a CSV dataset. This project includes data loading, visualization, and is Dockerized for easy deployment.

## Features
- Read and visualize data from CSV files.
- Dockerized application for easy setup and deployment.
- User-friendly interface for data interaction.

## Requirements
- Python 3.12
- Django
- Other dependencies listed in `requirements.txt`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Django_interview_project.git
   cd Django_interview_project
   
Install dependencies:

pip install -r requirements.txt

Build the Docker image:

docker build -t django_interview_project .

Run the Docker container:


docker run -p 8000:8000 django_interview_project

Access the application: Open your browser and go to http://localhost:8000/.
