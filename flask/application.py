# . .venv/bin/activate
from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask import request

application = Flask(__name__)
CORS(application)


# @application.route('/')  # Define la ruta
# def hello_world():
#     return "<h1>Hello wordl</h1>"  # Define respuesta


# @application.post('/')
# def hello_world2():
#     return render_template("./front/index.html")


# @application.route('/usuarios/<username>')  # Define la ruta
# def return_username(username):
#     return username  # Define respuesta


# # App para hacer TO-DO
# @application.post('/create-todo')
# def create_todo():
#     return "hola"


@application.get('/get-todos')
def get_todo():
    futbolistas = [{
        "todo": "hola"
    },
        {
        "todo": "adios"
    },
        {
        "todo": "el 3"
    }]
    return futbolistas


@application.post('/create-todo')
def parse_request():
    data = request.data  # data is empty
    print(data.decode())
    return "ok"
    # need posted data here
# @application.put('/create-todo')
# def complete_todo():
#     return "hola"
