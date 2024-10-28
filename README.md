# FastAPI Application

This project is a basic FastAPI application that exposes a simple API. The app returns "Hello World" on a GET request and is containerized using Docker.

## Features
- FastAPI for building the web API
- Docker for containerization
- Uvicorn as the ASGI server
- Robot Framework for automated testing

## Running with Docker
1. **Build Docker Image**
   ```bash
   docker build -t fastapi-app .
   ```
2. **Run Docker Container**
   ```bash
   docker run -d -p 8000:8000 fastapi-app
   ```

The app will now be accessible at [http://localhost:8000](http://localhost:8000).

## Testing with Robot Framework
This project includes automated tests written in Robot Framework.

### Installing Robot Framework
1. Open a terminal and run:
   ```bash
   pip install robotframework
   pip install robotframework-seleniumlibrary  # If you need Selenium
   ```

### Running Tests
1. Open a terminal in the project directory.
2. Execute the following command:
   ```bash
   robot test_suite.robot
   ```

### Test Results
After running the tests, check the generated files:
- `output.xml`
- `log.html`
- `report.html`

You can open these files in a web browser to view detailed test results.

