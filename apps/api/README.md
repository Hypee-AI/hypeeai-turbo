# HypeeAI API - FastAPI Backend

This is the FastAPI backend for the HypeeAI platform, providing authentication and social media integration services.

## Features

- Facebook OAuth integration using fastapi-sso
- JWT token-based authentication
- Endpoints for interacting with Facebook Pages

## Requirements

- Python 3.11+
- FastAPI
- fastapi-sso
- Facebook Developer Account

## Setup

### 1. Create a Python virtual environment

```bash
# From the project root directory
pnpm run setup
# Or manually
cd apps/api
uv venv
source .venv/bin/activate
uv pip install .
```

### 2. Create a Facebook App

1. Go to [Facebook for Developers](https://developers.facebook.com/)
2. Create a new app (Business type is recommended)
3. Add the "Facebook Login" product to your app
4. Configure Valid OAuth Redirect URIs:
   - Add `http://localhost:8000/v1/auth/callback/facebook` for local development
   - Add your production callback URL for production

### 3. Configure Environment Variables

Copy the example .env file and add your Facebook App credentials:

```bash
cp .env.example .env
# Edit the .env file with your Facebook App ID and Secret
```

Required variables:

- `FACEBOOK_CLIENT_ID`: Your Facebook App ID
- `FACEBOOK_CLIENT_SECRET`: Your Facebook App Secret
- `JWT_SECRET_KEY`: A secure key for signing JWTs

### 4. Run the Development Server

```bash
cd apps/api
uvicorn app.main:app --reload --port 8000
```

## API Documentation

Once the server is running, you can access the API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Authentication Flow

1. Frontend calls `/v1/auth/login/facebook` to get the login URL
2. User is redirected to Facebook to authorize the app
3. Facebook redirects to `/v1/auth/callback/facebook` with an authorization code
4. The API exchanges the code for an access token and user information
5. The API creates a JWT token and redirects to the frontend
6. Frontend uses the JWT token for authenticated API calls

## Available Endpoints

### Authentication

- `GET /v1/auth/login/facebook` - Get Facebook login URL
- `GET /v1/auth/callback/facebook` - Handle Facebook OAuth callback
- `POST /v1/auth/token/validate` - Validate a JWT token

### Facebook Integration

- `GET /v1/facebook/pages` - Get Facebook pages for the authenticated user
- `POST /v1/facebook/post` - Create a post on a Facebook page

## Development

### Project Structure

```bash
apps/api/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   └── v1/
│   │       └── routes/
│   │           ├── auth.py     # Authentication routes
│   │           ├── facebook.py # Facebook integration routes
│   │           └── ping.py     # Health check endpoint
│   ├── core/
│   │   ├── auth.py             # Authentication utilities
│   │   ├── config.py           # Application configuration
│   │   └── sso_providers.py    # SSO provider configuration
│   ├── models/
│   │   └── auth.py             # Data models for authentication
│   └── main.py                 # Application entry point
├── Dockerfile
├── pyproject.toml
├── README.md
├── uv.lock
```

---

## 🛠️ Local Development

### 1. Install Dependencies

Create a virtual environment

```bash
uv venv
source venv/bin/activate
```

Install dependencies

```bash
uv pip install -r pyproject.toml
```

(Or `uv pip install fastapi uvicorn` manually if fresh)

### 2. Start the Dev Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Swagger UI: http://localhost:8000/docs
- Redoc UI: http://localhost:8000/redoc

---

## 🔧 API Endpoints

| Method | Path        | Description             |
| :----: | :---------- | :---------------------- |
|  GET   | `/`         | Welcome message         |
|  GET   | `/v1/ping/` | Healthcheck (Ping-Pong) |

---

## 📦 Build & Run with Docker

```bash
docker build -t fastapi-backend .
docker run -p 8000:8000 fastapi-backend
```

---

## 🔄 TurboRepo Scripts

You can add scripts inside `package.json` and wire them in `turbo.json`.

Example `package.json`:

```json
{
  "scripts": {
    "dev": "uvicorn app.main:app --reload --port 8000",
    "lint": "ruff check . && black --check . && isort --check-only .",
    "format": "black . && isort ."
  }
}
```

Example `turbo.json`:

```json
{
  "pipeline": {
    "dev:api": {
      "dependsOn": [],
      "outputs": []
    }
  }
}
```

Run:

```bash
pnpm turbo run dev:api
```

---

## 📊 Tech Stack

- **FastAPI** - Web Framework
- **Uvicorn** - ASGI server
- **uv** - Python package manager
- **Pydantic** - Data validation
- **Docker** - Containerization
- **Turborepo** - Monorepo management
- **Ruff + Black + Isort** - Code linting and formatting
