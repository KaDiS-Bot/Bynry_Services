# Gas Utility Consumer Service API

## Overview
This Django-based API enables gas utility consumers to submit service requests, track their progress, and manage their accounts. The system also provides an admin dashboard for handling service requests efficiently.

## Features
- **User Authentication** (Signup/Login)
- **Service Request Submission & Tracking**
- **Consumer Account Management**
- **Admin Dashboard for Request Handling**

## Installation & Setup
### Prerequisites
- Python 3.x
- Django
- PostgreSQL (or SQLite for development)
- Git

### Steps
1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd gas-utility-service
   ```

2. **Create a Virtual Environment & Activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints
### Authentication
- `POST /api/register/` - Register a new user
- `POST /api/login/` - Authenticate user
- `POST /api/logout/` - Log out user

### Service Requests
- `POST /api/requests/` - Create a new service request
- `GET /api/requests/` - Get a list of all user requests
- `GET /api/requests/<id>/` - Get details of a specific request
- `PUT /api/requests/<id>/` - Update a service request
- `DELETE /api/requests/<id>/` - Delete a service request

### Admin Management
- `GET /api/admin/requests/` - View all service requests (Admin only)
- `PUT /api/admin/requests/<id>/status/` - Update request status

## Deployment
1. **Setup Environment Variables** (e.g., `.env` file)
2. **Run Database Migrations**
3. **Use a Production WSGI Server** (e.g., Gunicorn)

## Contribution
Feel free to fork and submit pull requests!

## License
MIT License

