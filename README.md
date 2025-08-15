Django Todo List Web Application
A clean, modern, and fully functional Todo List web application built with Django and styled with Bootstrap. This project allows users to manage their daily tasks through a simple and intuitive user interface with full CRUD (Create, Read, Update, Delete) functionality.

Features
Create Tasks: Quickly add new tasks to your list.

Read Tasks: View all your tasks in a clean, ordered list.

Update Tasks:

Mark tasks as complete or incomplete with a single click.

Edit the title of any existing task through a pop-up modal.

Delete Tasks: Remove tasks you no longer need.

Timestamps: Each task automatically displays its creation date.

Responsive Design: The application is fully responsive and works beautifully on desktops, tablets, and mobile devices.

Technology Stack
Backend: Django

Frontend: HTML, Bootstrap 5

Database: MySQL

Programming Language: Python

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You will need to have the following installed on your system:

Python 3.8+

pip (Python package installer)

A MySQL server instance

Installation
Clone the repository:

git clone https://github.com/your-username/TodoList-with-Django.git
cd TodoList-with-Django

Create and activate a virtual environment:

# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# For Windows
python -m venv .venv
.\.venv\Scripts\activate

Install the required Python packages:

pip install -r requirements.txt

Configure the database:

Create a new MySQL database named todolist_db.

Open the project/settings.py file.

Update the DATABASES dictionary with your MySQL username and password.

Run the database migrations:
This will create the necessary tables in your database.

python manage.py migrate

Run the development server:

python manage.py runserver

The application will be available at http://127.0.0.1:8000/.
