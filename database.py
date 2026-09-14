import sqlite3

DATABASE_NAME = "tasks.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
    """)

    connection.commit()

    task_count = connection.execute(
        "SELECT COUNT(*) FROM tasks"
    ).fetchone()[0]

    if task_count == 0:
        connection.executemany(
            """
            INSERT INTO tasks (title, done)
            VALUES (?, ?)
            """,
            [
                ("Learn FastAPI", 0),
                ("Build CRUD API", 0),
                ("Connect API to SQLite", 0),
            ]
        )

        connection.commit()

    connection.close()