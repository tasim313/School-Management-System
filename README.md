# School Management System

The School Management System is a Django-based web application designed to manage various aspects of a school, including student information, teacher details, and administrative tasks.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Setting up a Virtual Environment

1. Create a virtual environment (you may choose a different name):

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

### Installing Dependencies

Install the required Python packages using pip:

```bash
pip install -r development.txt

```


### Database Setup
python manage.py migrate


### Create a superuser account for administrative access:
python manage.py createsuperuser


### Running the Development Server
python manage.py runserver


### Project Structure
School: Main project folder.
SchoolAdminApp: Administrative functionalities.
StudentApp: Student-related functionalities.
TeacherApp: Teacher-related functionalities.
common: Shared components and utilities.
core: Core functionalities and settings.
school_auth: Authentication app.
