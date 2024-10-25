# FastAPI Application

This project is a basic FastAPI application that exposes a simple API. The app returns "Hello World" on a GET request and is containerized using Docker.

## Features
- FastAPI for building the web API
- Docker for containerization
- Uvicorn as the ASGI server

## Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn
```

### 3. Run the Application
```bash
uvicorn main:app --reload
```

Visit the app at `http://127.0.0.1:8000` and the API documentation at `http://127.0.0.1:8000/docs`.

## Running with Docker

### 1. Build Docker Image
```bash
docker build -t fastapi-app .
```

### 2. Run Docker Container
```bash
docker run -d -p 8000:8000 fastapi-app
```

The app will now be accessible at `http://localhost:8000`.

```

