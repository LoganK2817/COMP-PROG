import sqlite3

# Connect to the database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create the books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
''')

# Insert some data
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("1984", "George Orwell"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("To Kill a Mockingbird", "Harper Lee"))

# Commit the changes
conn.commit()

# Read and print all data
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()
