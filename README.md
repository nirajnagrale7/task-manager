# Task Manager API

A RESTful API for managing tasks, built using Django and Django REST Framework. This API allows users to create, update, and delete tasks, filter tasks by different parameters, and paginate results.

## 🛠️ Tech Stack

- **Framework**: Django, Django REST Framework
- **Database**: PostgreSQL (or MySQL)
- **Authentication**: JWT (JSON Web Token)
- **ORM**: Django ORM
- **Pagination**: Supported
- **Filters**: Status, Priority, Search, and Date Range

---

## 🚀 Setup Instructions

### Prerequisites

1. **Python 3.x** (preferably 3.8+)
2. **PostgreSQL** or **MySQL** (for production or local dev setup)
3. **Virtualenv** (recommended to create isolated environments)

---

### 🏗️ Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd task_manager
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure database in `settings.py` (update `DATABASES` section).
    For example:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'task_db',
            'USER': 'your_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access Django Admin:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:

    ```bash
    python manage.py runserver
    ```

---

## 🧑‍💻 API Endpoints

### Authentication

- **POST /api/token/** — Obtain JWT Token
  - Request body:
    ```json
    {
      "username": "admin_user",
      "password": "admin123"
    }
    ```

### Tasks

- **POST /api/tasks/** — Create a new task
  - Request body:
    ```json
    {
      "title": "Task 1",
      "description": "Description for Task 1",
      "status": 1,
      "priority": 2,
      "due_date": "2025-04-20"
    }
    ```
  - Response: 201 Created

- **GET /api/tasks/** — List tasks (with pagination & filtering)
  - Query params:
    - `status`: Filter by task status (1 to 4)
    - `priority`: Filter by priority (1 or 2)
    - `due_before`: Filter by due date
    - `due_after`: Filter by due date
    - `search`: Search tasks by title or description
    - `page`: For pagination (e.g., `page=2`)
  - Example:
    ```bash
    GET /api/tasks/?status=1&page=2
    ```

- **PUT /api/tasks/{id}/** — Update a task by ID
- **DELETE /api/tasks/{id}/** — Delete a task by ID

---

## 📝 Examples: cURL Commands

Here are example cURL commands for API usage:

1. **Login and get JWT Token**
    ```bash
    curl -X POST http://127.0.0.1:8000/api/token/ \
    -H "Content-Type: application/json" \
    -d '{"username": "admin_user", "password": "admin123"}'
    ```

2. **Create Task**
    ```bash
    curl -X POST http://127.0.0.1:8000/api/tasks/ \
    -H "Authorization: Bearer <your_token>" \
    -H "Content-Type: application/json" \
    -d '{"title": "New Task", "description": "Task description", "status": 1, "priority": 2, "due_date": "2025-05-01"}'
    ```

3. **List Tasks**
    ```bash
    curl -X GET http://127.0.0.1:8000/api/tasks/?page=1 \
    -H "Authorization: Bearer <your_token>"
    ```

---

## 📝 Postman Collection

1. **Import the following Postman collection** to get started quickly with API requests:
   [Download Postman Collection](<your_link_to_postman_collection_file>)

---

### 🎯 Features

- Secure token-based authentication using JWT
- Task management (CRUD operations)
- Filter tasks by status, priority, and due date
- Pagination and sorting of task lists

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




<!-- Updated -->

Here's the complete README.md file that includes everything for your project:

markdown
Copy
Edit
# Task Manager API Documentation

## Overview

This **Task Manager API** allows users to manage tasks assigned to them or by them. The API implements full authentication using JWT (JSON Web Tokens), task CRUD operations, pagination, filtering, and basic role-based permissions.

---

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- Django 5.x
- Django REST Framework
- PostgreSQL or MySQL (depending on the database you choose)
- `pip` (Python package manager)
- Postman (for testing APIs)

---

## Getting Started

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api
2. Create a Virtual Environment
Create and activate a virtual environment for the project:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
3. Install Dependencies
Install all the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Setup .env File
Create a .env file in the root directory of the project. The .env file contains environment variables for the database connection and secret keys.

Example .env file:
ini
Copy
Edit
# .env

# Django settings
DJANGO_SECRET_KEY=your-django-secret-key
DEBUG=True

# Database settings (PostgreSQL example)
DB_NAME=task_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

# JWT Secret Key (For token-based authentication)
JWT_SECRET_KEY=your-jwt-secret-key
Database Setup
This project uses PostgreSQL by default. Follow these steps to set up the database:

Install PostgreSQL on your local machine.

Create a new database:

bash
Copy
Edit
psql -U postgres
CREATE DATABASE task_db;
Configure the database settings in settings.py:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
Install the python-decouple package to manage environment variables more efficiently.

bash
Copy
Edit
pip install python-decouple
Update settings.py to use .env variables:

python
Copy
Edit
from decouple import config

SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

JWT_SECRET_KEY = config('JWT_SECRET_KEY')
Running the Project
1. Apply Migrations
Make sure all database migrations are applied:

bash
Copy
Edit
python manage.py migrate
2. Create Superuser
Create an admin superuser to access the Django admin panel:

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompt to set the username, email, and password.

3. Seed a User (Optional)
To seed a user for the initial setup (e.g., admin_user), run the following commands:

bash
Copy
Edit
python manage.py shell
In the Django shell, execute the following:

python
Copy
Edit
from django.contrib.auth.models import User
user = User.objects.create_user('admin_user', 'admin@example.com', 'admin123')
user.is_superuser = True
user.is_staff = True
user.save()
4. Run the Development Server
Start the development server:

bash
Copy
Edit
python manage.py runserver
Your project will be available at: http://127.0.0.1:8000/

API Endpoints
1. User Authentication (JWT)
Login (Obtain Token)

Endpoint: /api/login/
Method: POST
Request Body:

json
Copy
Edit
{
    "username": "admin_user",
    "password": "admin123"
}
Response:

json
Copy
Edit
{
    "access": "your-access-token",
    "refresh": "your-refresh-token"
}
Use the access token to authenticate subsequent requests.

Token Refresh

Endpoint: /api/refresh/
Method: POST
Request Body:

json
Copy
Edit
{
    "refresh": "your-refresh-token"
}
Response:

json
Copy
Edit
{
    "access": "new-access-token"
}
2. Task Endpoints
Create a Task

Endpoint: /api/tasks/
Method: POST
Headers:

json
Copy
Edit
{
    "Authorization": "Bearer your-access-token"
}
Request Body:

json
Copy
Edit
{
    "title": "Task 1",
    "description": "Description of Task 1",
    "status": 1,
    "priority": 2,
    "due_date": "2025-04-12",
    "assigned_by": "admin_user",
    "assigned_to": "john_doe"
}
Response:

json
Copy
Edit
{
    "id": 1,
    "title": "Task 1",
    "description": "Description of Task 1",
    "status": 1,
    "priority": 2,
    "due_date": "2025-04-12",
    "assigned_by": "admin_user",
    "assigned_to": "john_doe"
}
List Tasks

Endpoint: /api/tasks/
Method: GET
Headers:

json
Copy
Edit
{
    "Authorization": "Bearer your-access-token"
}
Query Parameters (Pagination & Filtering):

page: Page number (default: 1)

page_size: Number of items per page (default: 5)

status: Filter by task status

priority: Filter by task priority

due_before: Filter by tasks due before a specific date

due_after: Filter by tasks due after a specific date

search: Search by task title or description

Example request with pagination and filters:

bash
Copy
Edit
GET http://127.0.0.1:8000/api/tasks/?page=1&page_size=5&status=1&priority=2&search=task
Response:

json
Copy
Edit
{
    "count": 10,
    "next": "http://127.0.0.1:8000/api/tasks/?page=2&page_size=5",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Task 1",
            "description": "Task description",
            "status": 1,
            "priority": 2,
            "assigned_to": "john_doe"
        },
        {
            "id": 2,
            "title": "Task 2",
            "description": "Task description",
            "status": 2,
            "priority": 1,
            "assigned_to": "jane_smith"
        }
    ]
}
Retrieve Task by ID

Endpoint: /api/tasks/{task_id}/
Method: GET
Headers:

json
Copy
Edit
{
    "Authorization": "Bearer your-access-token"
}
Response:

json
Copy
Edit
{
    "id": 1,
    "title": "Task 1",
    "description": "Task description",
    "status": 1,
    "priority": 2,
    "assigned_by": "admin_user",
    "assigned_to": "john_doe"
}
Testing the API with Postman
Login and Get Token:

Set the request method to POST and the URL to http://127.0.0.1:8000/api/login/.

In the Body tab, use raw and select JSON. Input the credentials:

json
Copy
Edit
{
    "username": "admin_user",
    "password": "admin123"
}
Copy the access token from the response.

Create Task:

Set the request method to POST and the URL to http://127.0.0.1:8000/api/tasks/.

Go to the Authorization tab, choose Bearer Token, and paste the access token.

In the Body tab, use raw and select JSON. Input the task data.

Example:

json
Copy
Edit
{
    "title": "Task 1",
    "description": "Task description",
    "status": 1,
    "priority": 2,
    "due_date": "2025-04-12",
    "assigned_by": "admin_user",
    "assigned_to": "john_doe"
}
List Tasks:

Set the request method to GET and the URL to http://127.0.0.1:8000/api/tasks/.

Go to the Authorization tab and choose Bearer Token. Paste your access token.

Conclusion
Congratulations! You’ve successfully set up the Task Manager API and can now manage tasks with authentication, filtering, pagination, and more.

