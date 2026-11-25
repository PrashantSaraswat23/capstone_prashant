
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "reports",
    "chicago_crime.db"
)


def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn
