from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

from database import create_database, get_connection


app = FastAPI(
    title="Task API",
    description="A simple CRUD API built with FastAPI and SQLite.",
    version="2.0"
)


# Create the SQLite database and tasks table when the API starts
create_database()


# Stage 1: Root endpoint
@app.get(
    "/",
    description="Returns basic information about the Task API."
)
def root():
    return {
        "name": "Task API",
        "version": "2.0",
        "endpoints": ["/tasks"]
    }


# Stage 1: Health endpoint
@app.get(
    "/health",
    description="Checks whether the API is running."
)
def health():
    return {
        "status": "ok"
    }


# Request model for creating tasks
class TaskCreate(BaseModel):
    title: str


# Request model for updating tasks
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


# Stage 1: Get all tasks from SQLite
@app.get(
    "/tasks",
    description="Returns all tasks from the database."
)
def get_tasks():

    connection = get_connection()

    rows = connection.execute(
        "SELECT id, title, done FROM tasks ORDER BY id"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]


# Stage 1: Get one task from SQLite
@app.get(
    "/tasks/{task_id}",
    description="Returns a single task by ID."
)
def get_task(task_id: int):

    connection = get_connection()

    row = connection.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    return dict(row)


# Stage 2: Create a task in SQLite
@app.post(
    "/tasks",
    status_code=201,
    description="Creates a new task in the database."
)
def create_task(task: TaskCreate):

    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Task title cannot be empty"
        )

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO tasks (title, done)
        VALUES (?, ?)
        """,
        (task.title, False)
    )

    connection.commit()

    task_id = cursor.lastrowid

    row = connection.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    return dict(row)


# Stage 3: Update a task in SQLite
@app.put(
    "/tasks/{task_id}",
    description="Updates an existing task in the database."
)
def update_task(task_id: int, task: TaskUpdate):

    if task.title is None and task.done is None:
        raise HTTPException(
            status_code=400,
            detail="At least one field is required"
        )

    connection = get_connection()

    existing_task = connection.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if existing_task is None:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    if task.title is not None:

        if not task.title.strip():
            connection.close()

            raise HTTPException(
                status_code=400,
                detail="Task title cannot be empty"
            )

        connection.execute(
            "UPDATE tasks SET title = ? WHERE id = ?",
            (task.title, task_id)
        )

    if task.done is not None:

        connection.execute(
            "UPDATE tasks SET done = ? WHERE id = ?",
            (task.done, task_id)
        )

    connection.commit()

    updated_task = connection.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    return dict(updated_task)


# Stage 3: Delete a task from SQLite
@app.delete(
    "/tasks/{task_id}",
    status_code=204,
    description="Deletes an existing task from the database."
)
def delete_task(task_id: int):

    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    return Response(status_code=204)