from fastapi import FastAPI, HTTPException

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