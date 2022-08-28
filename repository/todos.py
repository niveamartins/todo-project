from errors.sql_errors import SQL_Exception
from .connection import get_db_connection
import sqlite3

def get_todos():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos').fetchall()
    conn.close()
    return todos

def create_todo(title):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
      cur.execute('INSERT INTO todos (title) VALUES (?)', (title,))
      conn.commit()
    except sqlite3.Error as er:
        return SQL_Exception()
    conn.close()
    return "Created a new todo task."