====================================================
           SQLITE TASK MANAGER PROJECT
====================================================

Author: Daniel

Description
-----------
This project is a beginner-friendly introduction to SQLite using Python.

The goal is to understand how Python communicates with a SQLite database,
how to create tables, insert data, retrieve data.

Unlike a Python list, the data is stored permanently inside a database file
(tasks.db), so it remains even after the program closes.

----------------------------------------------------
Project Structure
----------------------------------------------------

SQLite/
│
├── database.py
├── app.py (I included this so it will be used later when applying Flask logic)
├── tasks.db
└── README.txt

----------------------------------------------------
Topics Covered
----------------------------------------------------

✓ Importing the sqlite3 module
✓ Creating a SQLite database
✓ Creating a database connection
✓ Creating a cursor
✓ Creating a table
✓ SQL CREATE TABLE
✓ SQL INSERT
✓ SQL SELECT
✓ SQL UPDATE
✓ SQL DELETE
✓ fetchone()
✓ fetchall()
✓ commit()
✓ close()
✓ Parameterized Queries (?)
✓ SQL Injection Prevention

----------------------------------------------------
Database
----------------------------------------------------

Database Name:

tasks.db

Table Name:

tasks

Columns:

id            INTEGER PRIMARY KEY
title         TEXT NOT NULL
description   TEXT
completed     BOOLEAN DEFAULT 0
created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP

----------------------------------------------------
What I Learned
----------------------------------------------------

1. sqlite3.connect()

Creates a connection to the SQLite database.
If the database does not exist, SQLite automatically creates it.

----------------------------------------------------

2. cursor()

The cursor acts as a messenger between Python and SQLite.
It sends SQL commands to the database and returns the results.

----------------------------------------------------

3. execute()

Executes an SQL command.

Example:

cursor.execute("SELECT * FROM tasks")

----------------------------------------------------

4. commit()

Saves all changes permanently inside the database.

Without commit(), inserted or updated data may not be saved.

----------------------------------------------------

5. close()

Closes the database connection and releases the database file.

----------------------------------------------------

6. fetchall()

Returns every row from the query as a list of tuples.

Example:

[
    (1, "Learn SQLite"),
    (2, "Study Python")
]

----------------------------------------------------

7. fetchone()

Returns only the first matching row.

----------------------------------------------------

8. Parameterized Queries

Correct:

cursor.execute(
    "SELECT * FROM tasks WHERE id=?",
    (task_id,)
)

Never use:

cursor.execute(
    f"SELECT * FROM tasks WHERE id={task_id}"
)

Using ? placeholders protects the application against SQL Injection attacks.

----------------------------------------------------
CRUD Operations
----------------------------------------------------

CREATE

INSERT INTO tasks(title, description)
VALUES(?, ?)

----------------------------------------------------

READ

SELECT * FROM tasks

----------------------------------------------------
UPDATE

UPDATE tasks
SET title=?
WHERE id=?

----------------------------------------------------

DELETE

DELETE FROM tasks
WHERE id=?

----------------------------------------------------
Learning Goal
----------------------------------------------------

The purpose of this project is to understand SQLite before integrating it
with Flask.

====================================================
End of README
====================================================