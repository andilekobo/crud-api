# Task API

A RESTful CRUD API built with Python and FastAPI.

This project started as a simple in-memory CRUD API and was later upgraded to use SQLite for persistent data storage. The goal was to learn the fundamentals of API development first, then understand how a backend API connects to a real database.

## Features

- Create tasks
- Read all tasks
- Read a single task
- Update tasks
- Delete tasks
- Request validation with Pydantic
- HTTP error handling
- Automatic Swagger API documentation
- SQLite database persistence
- Automatic database and table creation
- SQL CRUD operations
- Database inspection using DB Browser for SQLite

## Tech Stack

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic
- SQLite
- SQL
- Git & GitHub
- DB Browser for SQLite

## Project Structure

```text
crud-api/
│
├── .venv/
├── .gitignore
├── database.py
├── main.py
├── README.md
└── tasks.db
