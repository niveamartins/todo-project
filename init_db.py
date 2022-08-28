import sqlite3

def init_db():
  connection = sqlite3.connect('database.db')

  with open('database.sql') as f:
    connection.executescript(f.read())

  cur = connection.cursor()

  cur.execute("INSERT INTO todos (title) VALUES ('Fazer API da Lacrei')")

  cur.execute("INSERT INTO todos (title) VALUES ('Enviar API para a Lacrei')")

  connection.commit()
  connection.close()