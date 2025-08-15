# Django Todo List Web Application

A clean, modern, and fully functional **Todo List** web application built with **Django** and styled with **Bootstrap 5**. This project allows users to manage their daily tasks through a simple and intuitive user interface with full **CRUD** (Create, Read, Update, Delete) functionality.

## ✨ Features

- **Create Tasks**: Quickly add new tasks to your list.
- **Read Tasks**: View all your tasks in a clean, ordered list.
- **Update Tasks**:
  - Mark tasks as complete or incomplete with a single click.
  - Edit the title of any existing task through a pop-up modal.
- **Delete Tasks**: Remove tasks you no longer need.
- **Timestamps**: Automatically display the creation date for each task.
- **Responsive Design**: Works beautifully on desktops, tablets, and mobile devices.

## 🛠 Technology Stack

- **Backend**: Django  
- **Frontend**: HTML, Bootstrap 5  
- **Database**: MySQL  
- **Programming Language**: Python  

## 🚀 Getting Started

Follow these instructions to set up the project locally for development and testing purposes.

### ✅ Prerequisites

Make sure you have the following installed:

- Python 3.8+
- pip (Python package installer)
- MySQL server instance

### 📥 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/TodoList-with-Django.git
    cd TodoList-with-Django
    ```

2. **Create and activate a virtual environment**:

    **macOS/Linux**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    **Windows**:
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database**:
    - Create a new MySQL database named `todolist_db`.
    - Open `project/settings.py`.
    - Update the `DATABASES` dictionary with your MySQL username and password.

5. **Run database migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:  
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
