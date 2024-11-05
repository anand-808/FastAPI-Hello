
# FastAPI with Cassandra & Robot Framework Integration

This project demonstrates the integration of **FastAPI** with **Apache Cassandra** for storing and retrieving user data, along with automated testing using **Robot Framework**.

## Features

- **POST /save_user/**: Save user information (name and email) to Cassandra.
- **GET /users/**: Retrieve all saved users from Cassandra and display them.
- **Dockerized**: Both FastAPI and Cassandra run in Docker containers.
- **Robot Framework**: Automated testing with logs and reports included.

## Project Structure

```
├── Dockerfile               # FastAPI Docker configuration
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Docker Compose for FastAPI and Cassandra
├── main.py                  # Main FastAPI application
├── app
│   ├── __init__.py          # App initialization
│   ├── models.py            # User data model
│   ├── db.py                # Cassandra connection and setup
│   └── routes.py            # API routes for saving and fetching data
├── robotests                # Robot Framework test cases and reports
│   ├── robo_test_cases.robot
│   ├── log.html
│   ├── report.html
│   ├── output.xml
│   └── test_main.py
└── README.md                # Project documentation
```

## Prerequisites

- **Docker**: Ensure Docker is installed on your system.
- **Python 3.10+**: Required if running the app locally without Docker.

## Setup and Run with Docker

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-cassandra.git
cd fastapi-cassandra
```

### 2. Build the Docker Images

```bash
docker-compose up --build
```

This will build and start two containers:
- **Cassandra**: The NoSQL database.
- **FastAPI**: The web framework that serves the API.

### 3. Running the Application

After building the images, the FastAPI server will be accessible at:

```bash
http://127.0.0.1:8000
```

You can interact with the API using the following endpoints:
- **GET** `/users/`: Retrieve all user data from Cassandra and display the entries in the database.
- **POST** `/save_user/`: Save a new user by sending a JSON payload like:

```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

### 4. Access API Documentation

FastAPI provides an interactive API documentation:

```bash
http://127.0.0.1:8000/docs
```

## Running Locally

To run the application locally without Docker:

1. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Start the FastAPI app:
    ```bash
    uvicorn main:app --reload
    ```

3. Make sure Cassandra is running and accessible on `localhost:9042`. You can start a Cassandra instance using Docker if needed:
    ```bash
    docker run --name cassandra-db -d -p 9042:9042 cassandra
    ```

## Database Setup (Cassandra)

When the FastAPI app starts, it automatically creates the `user_data_keyspace` and `users` table in Cassandra. You can interact with Cassandra directly using `cqlsh`:

```bash
docker exec -it cassandra-db cqlsh
```

### Create Keyspace and Table

First, create the keyspace and the table with the following commands:

```sql
CREATE KEYSPACE IF NOT EXISTS user_data_keyspace WITH REPLICATION = { 'class': 'SimpleStrategy', 'replication_factor': 1 };

USE user_data_keyspace;

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY,
    name TEXT,
    email TEXT
);
```

### Sample Insert Command

You can insert a sample user into the `users` table using the following CQL command:

```sql
INSERT INTO user_data_keyspace.users (id, name, email) VALUES (uuid(), 'Jane Doe', 'jane.doe@example.com');
```

### Verify User Entry

To verify the entry, use the following command to select all users:

```sql
SELECT * FROM user_data_keyspace.users;
```

## Automated Testing with Robot Framework

1. **Run Robot Framework Tests**

   To run automated tests, navigate to the `robotests` directory and run the Robot Framework tests:

   ```bash
   robot robotests/robo_test_cases.robot
   ```

2. **View Test Reports**

   After running the tests, reports are generated in the `robotests` folder:
   - `log.html`
   - `report.html`
   - `output.xml`

## Dependencies

**`requirements.txt`**

```
fastapi
uvicorn
cassandra-driver
robotframework
```

## API Endpoints

| Method | Endpoint         | Description                           |
|--------|------------------|---------------------------------------|
| POST   | /save_user/       | Save a user to Cassandra              |
| GET    | /users/           | Retrieve and display all users        |
| GET    | /                 | Test root endpoint                    |

## Troubleshooting

- **Connection Issues**: If Cassandra is not reachable, ensure the container is running and accessible via `localhost:9042`.
- **Logs**: You can check Docker logs for more details:
    ```bash
    docker logs fastapi-hello-cassandra
    docker logs cassandra-db
    ```

---

