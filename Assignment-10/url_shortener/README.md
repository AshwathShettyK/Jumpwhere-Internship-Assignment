# URL Shortener

A Django-based URL shortener that stores long URLs, generates unique short codes, redirects short links, and tracks click counts.

## Features

- Shorten long URLs
- Redirect shortened links
- Track click count
- Show recent links and creation date
- Admin interface for managing URLs
- Custom 404 page

## Folder Structure

- `project/` - Django project settings and URL configuration
- `shortener/` - Django app for URL shortening
- `templates/` - HTML templates for the app
- `static/` - CSS static files
- `media/` - Media storage folder

## Installation

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

Windows:

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

5. Start the development server:

```bash
python manage.py runserver
```

## Screenshots

Place screenshots in `docs/screenshots`.

## Future Improvements

- Add user authentication and personal link management
- Provide link expiration and analytics
- Add QR code generation
