# FastAPI Backend - TurboRepo Monorepo Setup

## 🚀 Overview

This is a production-ready **FastAPI** application structured for scalability inside a **Turborepo** monorepo.
Designed with future growth, modularity, and performance in mind.

---

## 📂 Project Structure

```bash
apps/api/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   └── v1/
│   │       └── routes/
│   │           └── ping.py
│   ├── core/
│   │   └── config.py
│   └── main.py
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
