# To-Do List App

A Django task manager app with task creation, editing, filtering, and task status management.

## Features

- Add, edit, and delete tasks
- Mark tasks complete or incomplete
- Search tasks by title or description
- Filter completed and pending tasks
- View task statistics
- Responsive Bootstrap interface

## Folder Structure

- `project/` - Django project configuration
- `todo/` - Django app with models, views, and forms
- `templates/` - HTML templates
- `static/` - CSS assets
- `media/` - optional media storage

## Installation

1. Create a Python virtual environment:

```bash
python -m venv .venv
```

2. Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

## Screenshots

Place screenshots in `docs/screenshots`.

## Future Improvements

- Add user accounts for personal task lists
- Add recurring task support
- Add calendar integration for due dates
