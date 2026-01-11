# Study Management Platform

A clean and simple web application for managing study topics with user authentication and hierarchical organization.

## Features

- User registration and authentication
- Create and organize study topics hierarchically
- Clean, responsive frontend interface
- Secure password storage with bcrypt
- JWT-based authentication system

## Prerequisites

- Python 3.13 or higher
- pip (Python package installer)
- uv (Python package manager) - optional but recommended

## Installation Instructions

### Option 1: Using pip (Standard Method)

1. Clone or download this repository to your local machine

2. Navigate to the project directory:
   ```bash
   cd /path/to/your/project
   ```

3. Install the required dependencies:
   ```bash
   pip install bcrypt fastapi[standard] passlib python-jose ruff sqlmodel uvicorn
   ```

### Option 2: Using uv (Recommended)

1. Install uv if you don't have it already:
   ```bash
   pip install uv
   ```

2. Navigate to the project directory:
   ```bash
   cd /path/to/your/project
   ```

3. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Running the Application

1. Make sure you're in the project directory (`/workspace`)

2. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   Alternatively, if you installed dependencies with pip instead of uv:
   ```bash
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. Open your browser and go to:
   - Frontend Interface: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## How to Use

1. Register a new account using the registration form
2. Log in with your credentials
3. Use the dashboard to create and manage study topics
4. Organize topics hierarchically using the parent-child relationship feature
5. Manage your study plan efficiently through the intuitive interface

## Project Structure

```
/workspace/
├── main.py                 # Main FastAPI application
├── index.html              # Frontend interface
├── pyproject.toml          # Project dependencies
├── model/                  # Database models
│   ├── assunto.py          # Subject model
│   ├── usuario.py          # User model
│   └── ...                 # Other models
├── routes/                 # API routes
│   ├── usuarios.py         # User routes
│   ├── token.py            # Authentication routes
│   └── assuntos.py         # Subject routes
└── utilidades/             # Utility functions
    ├── database.py         # Database utilities
    └── seguranca.py        # Security utilities
```

## Troubleshooting

If you encounter issues:

1. Make sure you have Python 3.13 or higher installed:
   ```bash
   python --version
   ```

2. Check that all dependencies are properly installed:
   ```bash
   pip list
   ```

3. If you get permission errors, try running with administrator privileges or in a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install bcrypt fastapi[standard] passlib python-jose ruff sqlmodel uvicorn
   ```

4. Make sure port 8000 is available and not used by another application

## Security Notes

- Passwords are securely hashed using bcrypt
- Authentication uses JWT tokens
- CORS is configured to allow all origins (in development only)
- Always use HTTPS in production environments

## Technologies Used

- FastAPI: Modern, fast web framework for building APIs
- SQLModel: SQL database modeling library
- bcrypt: Password hashing
- Passlib: Password hashing library
- Python-Jose: JWT token handling
- Uvicorn: ASGI server for running the application