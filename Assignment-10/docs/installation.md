# Installation Guide

This repository includes three Django projects under `Assignment-10`:

- `url_shortener`
- `todo_app`
- `english_dictionary`

## Requirements

- Python 3.13+
- Django 6.x
- SQLite (default database)

## General Setup

1. Open a terminal in `Assignment-10`.
2. Create a virtual environment for each project or one shared environment.
3. Activate the environment.
4. Install dependencies from the `requirements.txt` file inside each project.
5. Run `python manage.py migrate` for each project.
6. Run `python manage.py runserver` inside each project folder.

## Running Projects

Example for `url_shortener`:

```bash
cd url_shortener
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Repeat for `todo_app` and `english_dictionary`.
