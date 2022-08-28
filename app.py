from flask import Flask, request
from controllers.todos import index, create
from init_db import init_db

app = Flask(__name__)

init_db()

@app.route('/todos', methods=('GET', 'POST'))
def control():
  if request.method == 'GET':
      return index()
  else:
      return create(request)
