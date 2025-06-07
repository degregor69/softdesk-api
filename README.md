# SoftDesk API

A secure RESTful API for project, issue, and comment management, built with Django REST Framework.

## Key Features

- JWT-based user authentication
- User registration with age verification and GDPR consent
- Project creation and management
- Contributor management per project
- Issue tracking (priority, status, tags)
- Comment system on issues
- Role-based permissions (author, contributor)
- Automatic pagination of resource listings

## Installation

### Prerequisites

- Python 3.13+
- [Poetry](https://python-poetry.org/)
- Git

### Setup



```bash
git clone https://github.com/degregor69/softdesk-api.git
cd softdesk-api 
```
You can create a virtual environment if you want. 
I personally use pyenv

```bash
pyenv virtualenv 3.13.3 venv
pyenv activate venv
```
Then continue : 
```bash
poetry install
python manage.py migrate
python manage.py runserver
```

> The API will be available at http://localhost:8000

## Authentication
Authentication is handled via JWT.

> POST /api/token/

```bash
{
  "username": "your_username",
  "password": "your_password"
}
```

Include the token in the Authorization header for all protected endpoints:

> Authorization: Bearer <your_token>

You can enjoy the app.

## License

MIT License
Developed as part of an OpenClassrooms project.