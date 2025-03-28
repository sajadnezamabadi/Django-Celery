# Django-Celery

This project is a Django application integrated with Celery and Redis for managing background tasks.

## Features

- Built with Django 4.2
- Celery for background task management
- Redis as the message broker
- Docker and Docker Compose for container management

## Prerequisites

To run this project, you need to have the following installed:

- [Docker](https://www.docker.com/)  
- [Docker Compose](https://docs.docker.com/compose/)

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Django-Celery

2.

  Configure the .env file with the required environment variables:

      DEBUG
      ALLOWED_HOSTS
      CELERY_BROKER_URL
      CELERY_BACKEND

3.
  Build and start the containers using Docker Compose:
      docker-compose exec django python manage.py migrate
      docker-compose exec celery celery -A dcelery worker --loglevel=info
      docker-compose up --build
      

The Django application will be available at:

            http://localhost:8001













      
