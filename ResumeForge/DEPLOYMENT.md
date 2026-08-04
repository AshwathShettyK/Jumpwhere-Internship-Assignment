# ResumeForge Deployment Guide

## Overview
This document describes deployment options for the ResumeForge Django application.

## Prerequisites
- Python 3.14
- Docker and Docker Compose (for container deployment)
- A MySQL database for production
- Environment variables configured in `.env`

## Environment Variables
Create a `.env` file using `.env.example` as a template.

Required variables:
- `SECRET_KEY`
- `DEBUG` (set to `False` in production)
- `MYSQL_DATABASE`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `MYSQL_HOST`
- `MYSQL_PORT`

## Local Development
Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```
```

Run the development server:

```bash
python manage.py runserver
```

## Docker Deployment
Build and start containers:

```bash
docker compose up --build
```

The app will be available at `http://localhost:8000`.

## Heroku and PaaS
The repository includes a `Procfile` and `runtime.txt` for compatibility with Heroku-like platforms.

### Recommended production settings
- `DEBUG=False`
- `ALLOWED_HOSTS` set to your hostnames
- Configure a secure `SECRET_KEY`
- Use a managed MySQL or PostgreSQL database
- Configure static file hosting or use `whitenoise`

## Notes
- Static files are served from `/static/`
- Media files are stored in `/media/`
- Use `gunicorn` for production WSGI serving
