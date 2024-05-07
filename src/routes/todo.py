from flask import Blueprint
from services.todo import create_todo_service, get_todos_service

todo = Blueprint('todo', __name__)

@todo.route('/', methods=['GET'])
def get_todos():
    return get_todos_service()

@todo.route('/<id>', methods=['GET'])
def get_todo(id):
    return 'Get todo by id'

@todo.route('/', methods=['POST'])
def create_todo():
    return create_todo_service()

@todo.route('/<id>', methods=['PUT'])
def update_todo(id):
    return 'Update todo'

@todo.route('/<id>', methods=['DELETE'])
def delete_todo(id):
    return 'Delete todo'
