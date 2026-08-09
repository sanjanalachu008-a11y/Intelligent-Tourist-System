import sqlite3
import os

# Find the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SQLite database path
DB_PATH = os.path.join(BASE_DIR, "tourist_project.db")

# Create database connection
connection = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)

# Return rows like dictionaries
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

print("SQLite database connected successfully!")