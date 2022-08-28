from repository.todos import get_todos, create_todo
from flask import jsonify
from schemas.todo import validate_todo

def index():
    result = get_todos()
    response = []
    for todo in result:
        response.append(
            {
                "id": todo["id"],
                "title": todo["title"],
                "created_on": todo["created"]
            }
        )
    return jsonify(response)

def create(request):
    data = request.json
    try:
      validate_todo(data)
    except ValueError as er:
      return str(er)
    return create_todo(data["title"])