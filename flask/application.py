from flask import Flask

application = Flask(__name__)


@application.route('/')  # Define la ruta
def hello_world():
    return "<h1>Hello wordl</h1>"  # Define respuesta


@application.route('/usuarios/<username>')  # Define la ruta
def return_username(username):
    return username  # Define respuesta
