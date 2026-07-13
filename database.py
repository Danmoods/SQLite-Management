import sqlite3

# Connect
conn = sqlite3.connect("tasks.db")

# Cursor
cursor = conn.cursor()

# Read all tasks
cursor.execute("SELECT * FROM tasks")

# Store the results
rows = cursor.fetchall()

# Display each row
for row in rows:
    print(row)

# Close database
conn.close()

print("Data retrieved successfully.")