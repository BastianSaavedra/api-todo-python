from config.mongodb import mongo
from flask import request, Response
from bson import json_util


def create_todo_service():
    data = request.get_json()
    title = data.get('title', None) #
    description = data.get('description', None)
    if title:
        response = mongo.db.todos.insert_one({
            'title': title,
            'description': description,
            'done': False
        })
        result = {
            'id': str(response.inserted_id),
            'title': title,
            'description': description,
            'done': False
        }
        return result
    else:
        return 'Invalid payload', 400 # 400: Bad request


def get_todos_service():
    data = mongo.db.todos.find()
    result = json_util.dumps(data)
    return Response(result, mimetype="application/json")


