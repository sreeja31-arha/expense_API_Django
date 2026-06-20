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

## Running with Docker

This project is fully containerized for consistent, environment-independent deployment.

### Prerequisites
- Docker Desktop installed and running

### Build the image
```bash
docker build -t expense-api .
```

### Run the container
```bash
docker run -d -p 8000:8000 --name expense-api-container expense-api
```

### Access the API
- Swagger documentation: `http://localhost:8000/api/docs/`
- Admin panel: `http://localhost:8000/admin/`

### Stop the container
```bash
docker stop expense-api-container
```

### Tech stack in container
- Python 3.12
- Django 6.0.5
- Django REST Framework
- JWT Authentication
- drf-spectacular (OpenAPI/Swagger docs)