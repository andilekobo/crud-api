from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel


app = FastAPI()


# Stage 1: Root endpoint
@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


# Stage 1: Health endpoint
@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# Stage 3: Request model for creating tasks
class TaskCreate(BaseModel):
    title: str


# Stage 4: Request model for updating tasks
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


# Stage 2: In-memory tasks
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Build CRUD API",
        "done": False
    },
    {
        "id": 3,
        "title": "Push project to GitHub",
        "done": False
    }
]


# Stage 2: Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# Stage 2: Get one task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )


# Stage 3: Create a task
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    # Validate title
    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Task title cannot be empty"
        )

    # Generate next ID
    new_id = max(
        existing_task["id"]
        for existing_task in tasks
    ) + 1

    # Create task
    new_task = {
        "id": new_id,
        "title": task.title,
        "done": False
    }

    # Add task to list
    tasks.append(new_task)

    return new_task


# Stage 4: Update a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):

    # Find the task
    for existing_task in tasks:

        if existing_task["id"] == task_id:

            # Make sure at least one field was provided
            if task.title is None and task.done is None:
                raise HTTPException(
                    status_code=400,
                    detail="At least one field is required"
                )

            # Validate title if provided
            if task.title is not None:

                if not task.title.strip():
                    raise HTTPException(
                        status_code=400,
                        detail="Task title cannot be empty"
                    )

                existing_task["title"] = task.title

            # Update done if provided
            if task.done is not None:
                existing_task["done"] = task.done

            return existing_task

    # Task does not exist
    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )


# Stage 4: Delete a task
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:

            tasks.pop(index)

            return Response(status_code=204)

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )