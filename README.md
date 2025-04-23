# To-Do List Backend

This is the backend server for the To-Do List app built with Django REST Framework.

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Run the development server:

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/tasks/`.

## Deployment on Render

- Create a new Web Service on Render.
- Connect your GitHub repository.
- Set the build command to:

```bash
pip install -r requirements.txt && python manage.py migrate
```

- Set the start command to:

```bash
gunicorn todo_backend.wsgi
```

- Make sure to add environment variables for `SECRET_KEY` and `DEBUG` as needed.

## API Endpoints

- `GET /api/tasks/` - List all tasks, supports filtering by `completed` status.
- `POST /api/tasks/` - Create a new task.
- `GET /api/tasks/{id}/` - Retrieve a task.
- `PUT /api/tasks/{id}/` - Update a task.
- `DELETE /api/tasks/{id}/` - Delete a task.

## Notes

- CORS is enabled for all origins for development purposes.
- Use environment variables and proper settings for production deployment.
