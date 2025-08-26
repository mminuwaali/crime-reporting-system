---
description: Repository Information Overview
alwaysApply: true
---

# Crime Reporting System Information

## Summary
A Django-based web application for crime reporting, featuring user account management and core reporting functionality. The project uses Django 5.2.5 with TailwindCSS for frontend styling.

## Structure
- **website/**: Main Django project configuration files
- **account/**: Django app for user authentication and account management
- **coreapp/**: Django app for core crime reporting functionality
- **themes/**: TailwindCSS configuration and styling resources
- **.env/**: Python virtual environment

## Language & Runtime
**Language**: Python
**Version**: Python 3.12.3
**Framework**: Django 5.2.5
**Package Manager**: pip

## Dependencies
**Main Dependencies**:
- Django 5.2.5
- django-tailwind 4.2.0
- asgiref 3.9.1
- sqlparse 0.5.3

**Frontend Dependencies**:
- TailwindCSS 4.1.11
- PostCSS 8.5.6

**Development Dependencies**:
- django-browser-reload 1.18.0
- cross-env 7.0.3
- postcss-cli 11.0.1
- rimraf 6.0.1

## Build & Installation
```bash
# Create and activate virtual environment
python -m venv .env
source .env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd themes/static_src
npm install

# Build frontend assets
npm run build

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

## Development
```bash
# Run Django development server
python manage.py runserver

# Run TailwindCSS in watch mode
python manage.py tailwind start

# Run both simultaneously
honcho -f Procfile.tailwind start
```

## Database
**Engine**: SQLite3
**Configuration**: Default Django SQLite configuration
**Location**: db.sqlite3 in project root

## Frontend
**Framework**: TailwindCSS 4.1.11
**Build System**: npm with PostCSS
**Template Engine**: Django Templates
**Base Template**: themes/templates/base.html

## Project Components
- **Account App**: Handles user authentication, registration, and profile management
- **Core App**: Manages crime reporting functionality
- **Themes App**: Custom Django app for TailwindCSS integration