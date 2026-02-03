# Django To-Do List Web Application

A simple, fully responsive To-Do List web app built with Django (backend), Bootstrap 5, HTML, and CSS (frontend). Users can securely manage daily tasks with authentication.

## Features

### User Authentication
- User registration
- User login
- User logout

### Task Management
- Add new tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed or incomplete
- Each user can view and manage only their own tasks

### Functional Requirements
- Task fields: Title, Description (optional), Status (completed/pending), Created date
- Tasks linked to the logged-in user
- Only authenticated users can access the dashboard
- Unauthenticated users are redirected to the login page

### UI / UX
- Clean, minimal, and fully responsive design
- Bootstrap navbar with app name, Add Task, and Logout button
- Task list displayed using Bootstrap cards or tables
- Completed tasks visually differentiated (strike-through or badge)
- Simple forms using Bootstrap styling
- Footer with basic info

### Technical
- Django project with reusable apps: `accounts` (authentication), `tasks` (task management)
- Django ORM with SQLite database
- Django templates with Bootstrap 5
- Static files configuration
- Minimal custom CSS
- Beginner-friendly, well-commented code

## Getting Started

1. **Clone the repository**
2. **Create and activate a virtual environment**
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
6. **Open** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) **in your browser**

## Folder Structure
- `accounts/` - User authentication (register, login, logout)
- `tasks/` - Task management (CRUD, user-only access)
- `templates/` - HTML templates (Bootstrap 5)
- `static/` - Static files (Bootstrap, custom CSS)

## Notes
- For production, set `DEBUG = False` and configure allowed hosts and static files properly.
- This project is for educational/demo purposes.

---

&copy; 2026 To-Do List App. All rights reserved.
=======
# To-do-list
>>>>>>> de72a96212c68c3a2e42bcdf03c0d2fd80e9608f
 # Django To-Do List Web Application

A simple, fully responsive To-Do List web app built with Django (backend), Bootstrap 5, HTML, and CSS (frontend). Users can securely manage daily tasks with authentication.

## Features

### User Authentication
- User registration
- User login
- User logout

### Task Management
- Add new tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed or incomplete
- Each user can view and manage only their own tasks

### Functional Requirements
- Task fields: Title, Description (optional), Status (completed/pending), Created date
- Tasks linked to the logged-in user
- Only authenticated users can access the dashboard
- Unauthenticated users are redirected to the login page

### UI / UX
- Clean, minimal, and fully responsive design
- Bootstrap navbar with app name, Add Task, and Logout button
- Task list displayed using Bootstrap cards or tables
- Completed tasks visually differentiated (strike-through or badge)
- Simple forms using Bootstrap styling
- Footer with basic info

### Technical
- Django project with reusable apps: `accounts` (authentication), `tasks` (task management)
- Django ORM with SQLite database
- Django templates with Bootstrap 5
- Static files configuration
- Minimal custom CSS
- Beginner-friendly, well-commented code

## Getting Started

1. **Clone the repository**
2. **Create and activate a virtual environment**
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
6. **Open** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) **in your browser**

## Folder Structure
- `accounts/` - User authentication (register, login, logout)
- `tasks/` - Task management (CRUD, user-only access)
- `templates/` - HTML templates (Bootstrap 5)
- `static/` - Static files (Bootstrap, custom CSS)

## Notes
- For production, set `DEBUG = False` and configure allowed hosts and static files properly.
- This project is for educational/demo purposes.

---

&copy; 2026 To-Do List App. All rights reserved.
