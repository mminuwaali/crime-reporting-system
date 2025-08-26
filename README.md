# Crime Reporting System

This is a web-based application for reporting and managing crime complaints. It allows users to create accounts, file complaints, and track their status.

## Features

*   **User Authentication:** Users can sign up, sign in, and sign out. They can also manage their profile and change their password.
*   **Complaint Management:** Users can create, view, update, and delete their complaints.
*   **Complaint Tracking:** Complaints have different statuses (e.g., pending, investigating, resolved, closed) that users can track.
*   **Evidence Upload:** Users can upload evidence related to their complaints.
*   **Dashboard:** Users have a dashboard to see an overview of their complaints.

## Dependencies

The project's dependencies are listed in the `requirements.txt` file. The main dependencies are:

*   Django
*   django-tailwind
*   django-browser-reload

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/mminuwaali/crime_reporting_system.git
    cd crime_reporting_system
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv .env
    source .env/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Install the tailwindcss dependencies:**

    ```bash
    npm install
    ```

5.  **Apply the database migrations:**

    ```bash
    python manage.py migrate
    ```

## Running the Project

1.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

2.  **Start the tailwindcss server:**

    ```bash
    python manage.py tailwind start
    ```

3.  Open your web browser and go to `http://127.0.0.1:8000/` to see the application.

## Project Structure

The project is organized into the following apps:

*   `account`: Handles user authentication and profile management.
*   `coreapp`: Contains the core functionality of the crime reporting system.
*   `themes`: Manages the project's theme and static files.
*   `website`: The main Django project folder.
