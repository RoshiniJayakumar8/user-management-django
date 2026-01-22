# User Management System (Django + DRF)

## Project Description
A secure User Management System built using Django and Django REST Framework.
This project implements JWT-based authentication, an admin dashboard, role-based
access control, and REST APIs for managing users.

The system allows users to register and login securely, while administrators can
view, search, update, and delete users through protected APIs and the Django admin panel.

---

## Tech Stack
- Python 3.10
- Django 5.x
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite (Development Database)

---

## Features Implemented
- Custom User Model with extended fields
- User Registration with input validation
- JWT Authentication (Access & Refresh tokens)
- Admin Panel (Django Admin Dashboard)
- Admin-only User CRUD APIs
- Role-based Access Control (RBAC)
- Search & Filter (name, email, city, state)
- Pagination
- Profile Image Upload
- Secure Password Hashing
- Proper Error Handling

---

## Project Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd user_management
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment
venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
5. Run Database Migrations
python manage.py makemigrations
python manage.py migrate
6. Create Admin User
python manage.py createsuperuser
7. Run Development Server
python manage.py runserver
Admin Panel
Access the Django Admin Panel at:
http://127.0.0.1:8000/admin
Admin users can:
*View all users
*Edit user details
*Delete users
API Endpoints
Authentication APIs
Method	    Endpoint	Description
POST	/api/auth/register/	Register a new user
POST	/api/auth/login/	Login and get JWT tokens
POST	/api/auth/refresh/	Refresh access token
User Management APIs (Admin Only)
Method	   Endpoint	Description
GET	/api/users/	List users (paginated)
GET	/api/users/{id}/	Get user details
PUT	/api/users/{id}/	Update user
DELETE	/api/users/{id}/	Delete user
________________________________________
Authentication & Authorization
All protected APIs require JWT authentication.
Add the following header in Postman:
Authorization: Bearer <ACCESS_TOKEN>
Notes
•	Database file (db.sqlite3) is excluded intentionally
•	Migration files are included to recreate schema
•	Admin login and User API login are separate by design
Postman documentation link:
https://roshinij489-2029387.postman.co/workspace/Roshini-Jayakumar's
