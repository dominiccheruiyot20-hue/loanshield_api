# 🛡️ LoanShield API - Loan Fraud Detection

Live: https://loanshield-api-92gi.onrender.com/
Admin: https://loanshield-api-92gi.onrender.com/admin

LoanShield is a Django REST Framework API that detects fraudulent loan applications using Machine Learning.

## Features
- ML Fraud Detector (`fraud_detector/`)
- REST API endpoints
- Django Admin with custom login
- Deployed on Render with PostgreSQL/SQLite
- Auto superuser creation for production

## Stack
Django 5.x • DRF • scikit-learn • Render • Gunicorn • Whitenoise

## API Endpoints
- `/admin/` - Admin dashboard
- `/api/` - Your fraud prediction endpoints

## Deploy on Render
Build Command:
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py createsuperuser --noinput || true

Start Command:
gunicorn loanshield_api.wsgi:application

Environment Variables:
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
SECRET_KEY
DEBUG=False

## Local Dev
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Author
Dominic Cheruiyot (dominiccheruiyot20@gmail.com)
Kenya • 2026
