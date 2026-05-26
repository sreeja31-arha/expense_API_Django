# Expenses REST API

A production-ready REST API built with Django REST Framework 
featuring JWT authentication and user-specific data management.

## Features
- User registration and JWT login
- Full CRUD for expense management
- User specific data isolation
- Expense summary endpoint
- Consistent JSON response structure
- Input validation and error handling

## Tech Stack
Python | Django | Django REST Framework | JWT | SQLite

## Setup Instructions

### 1. Clone the repository
git clone <your repo url>
cd expenses-api

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run migrations
python manage.py migrate

### 5. Run server
python manage.py runserver

## API Endpoints

### Auth
| Method | URL | Description |
|--------|-----|-------------|
| POST | /api/auth/register/ | Register new user |
| POST | /api/auth/login/ | Login and get tokens |
| POST | /api/auth/token/refresh/ | Refresh access token |

### Expenses
| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/expenses/ | Get all expenses |
| POST | /api/expenses/ | Create expense |
| GET | /api/expenses/summary/ | Get expense summary |
| GET | /api/expenses/<id>/ | Get one expense |
| PUT | /api/expenses/<id>/ | Update expense |
| DELETE | /api/expenses/<id>/ | Delete expense |

## Sample Response

### Success
{
    "status": "success",
    "message": "Expenses fetched successfully",
    "data": [...]
}

### Error
{
    "status": "error",
    "message": "Validation failed",
    "errors": {...}
}