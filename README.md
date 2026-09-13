# Task API

A simple CRUD REST API built with **Python and FastAPI**.

This project was built as part of the FlyRank Backend AI Engineering track to practice the fundamentals of building, testing, documenting, and version-controlling a backend API.

## Features

* Create tasks
* Read all tasks
* Read a single task
* Update tasks
* Delete tasks
* Input validation
* Proper HTTP status codes
* Interactive Swagger API documentation
* In-memory data storage
* Git version control with staged commits

## Tech Stack

* Python 3.14
* FastAPI
* Uvicorn
* Pydantic
* Git

## Project Structure

```text
crud api/
├── .venv/
├── .gitignore
├── main.py
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd "crud api"
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

### 5. Start the API

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Swagger Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

From Swagger UI, you can test all of the API endpoints directly from your browser.

## API Endpoints

| Method | Endpoint           | Description             | Success |
| ------ | ------------------ | ----------------------- | ------- |
| GET    | `/`                | Returns API information | 200     |
| GET    | `/health`          | Checks API health       | 200     |
| GET    | `/tasks`           | Returns all tasks       | 200     |
| GET    | `/tasks/{task_id}` | Returns one task        | 200     |
| POST   | `/tasks`           | Creates a task          | 201     |
| PUT    | `/tasks/{task_id}` | Updates a task          | 200     |
| DELETE | `/tasks/{task_id}` | Deletes a task          | 204     |

## Example Task

A task has the following structure:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

## CRUD Examples

### Create a task

**POST `/tasks`**

Request:

```json
{
  "title": "Buy milk"
}
```

Response:

```json
{
  "id": 4,
  "title": "Buy milk",
  "done": false
}
```

The API returns:

```text
201 Created
```

The server automatically assigns the task ID and sets `done` to `false`.

### Get all tasks

**GET `/tasks`**

Example response:

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "done": false
  },
  {
    "id": 2,
    "title": "Build CRUD API",
    "done": false
  }
]
```

### Get one task

**GET `/tasks/1`**

Example response:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

If the task does not exist, the API returns:

```text
404 Not Found
```

Example:

```json
{
  "detail": "Task 99 not found"
}
```

### Update a task

**PUT `/tasks/1`**

Request:

```json
{
  "title": "Learn FastAPI properly",
  "done": true
}
```

Response:

```json
{
  "id": 1,
  "title": "Learn FastAPI properly",
  "done": true
}
```

The API returns:

```text
200 OK
```

### Delete a task

**DELETE `/tasks/1`**

The task is removed from the in-memory task list.

The API returns:

```text
204 No Content
```

## Validation

The API validates task input before creating or updating tasks.

For example, an empty title is rejected:

```json
{
  "title": ""
}
```

Response:

```text
400 Bad Request
```

```json
{
  "detail": "Task title cannot be empty"
}
```

Updating a task without providing any fields is also rejected.

## Error Handling

The API uses appropriate HTTP status codes:

| Status | Meaning                       |
| ------ | ----------------------------- |
| 200    | Request successful            |
| 201    | Resource successfully created |
| 204    | Resource successfully deleted |
| 400    | Invalid request               |
| 404    | Task not found                |

## Data Storage

This project currently uses an **in-memory Python list** to store tasks.

This was intentional for the assignment so that the focus could remain on understanding the fundamentals of REST APIs and CRUD operations.

Because the data is stored in memory, tasks are reset whenever the server restarts.

A future version could replace the in-memory storage with a database such as:

* PostgreSQL
* SQL Server
* SQLite

## Development Process

The API was developed incrementally through separate Git commits.

The stages included:

```text
Stage 0: hello server
Stage 1: root and health endpoints
Stage 2: read endpoints with 404
Stage 3: create with validation
Stage 4: full CRUD
Stage 5: Swagger UI
```

This approach made it possible to test each part of the API before moving to the next stage.

## What I Learned

Through this project I practiced:

* How REST APIs work
* HTTP methods and status codes
* FastAPI routing
* Path parameters
* Request bodies
* Pydantic models
* Input validation
* Error handling
* CRUD operations
* Swagger/OpenAPI documentation
* Running APIs with Uvicorn
* Git commits and version control

## Future Improvements

Possible improvements for a future version include:

* Add a persistent database
* Add authentication and authorization
* Add automated tests with Pytest
* Add pagination
* Add filtering and searching
* Containerize the application with Docker
* Deploy the API to a cloud platform
* Add CI/CD with GitHub Actions

## API Documentation

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative OpenAPI documentation:

```text
http://127.0.0.1:8000/redoc
```

## Assignment

Built as part of the **FlyRank Backend AI Engineering** learning track.

The project focuses on demonstrating practical backend fundamentals through a working REST API.

## Author

**Andile Koboti**

GitHub: `https://github.com/andilekobo`
