from flask import Flask, request, jsonify
from service import ToDoService
from models import Schema

import json

newApp = Flask(__name__)


@newApp.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response


@newApp.route("/")
def hello():
    return "Hello World!"


@newApp.route("/<name>")
def hello_name(name):
    return "Hello " + name


@newApp.route("/todo", methods=["GET"])
def list_todo():
    return jsonify(ToDoService().list())


@newApp.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))


@newApp.route("/todo/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(ToDoService().update(item_id, request.get_json()))


@newApp.route("/todo/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify(ToDoService().delete(item_id))


if __name__ == "__main__":
    Schema()
    newApp.run(debug=True, host='0.0.0.0', port=8888)
