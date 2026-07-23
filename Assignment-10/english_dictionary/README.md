# English Dictionary

A Django dictionary app that searches English words, retrieves definitions, parts of speech, examples, synonyms, and antonyms.

## Features

- Search English words
- Display multiple definitions
- Show parts of speech and examples
- Display synonyms and antonyms
- Handle invalid words gracefully
- Responsive Bootstrap layout

## Folder Structure

- `project/` - Django project configuration
- `dictionary/` - Django app with search and detail views
- `templates/` - HTML templates
- `static/` - CSS assets
- `media/` - optional media storage

## Installation

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

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

- Add search history and recent searches
- Cache API results locally for faster response
- Add audio pronunciation support
