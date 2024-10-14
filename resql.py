import os
import sqlite3
# Create the database connection
conn = sqlite3.connect("student.db")

# Perform your database operations here

# Close the connection when done
conn.close()


# Delete the database file
os.remove("student.db")
