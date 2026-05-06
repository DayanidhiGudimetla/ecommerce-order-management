import sqlite3

DB_NAME = "ecommerce.db"

def connect():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row  # Allows dict-like access to rows
    return conn
