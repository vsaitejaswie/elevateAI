from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_tej():
    return "<p>Hello, Tej!</p>"

@app.route('/hello')
def hello_world_static():
    return 'Hello, World'

@app.route("/<name>")
def hello_name(name):
    return f"Hello, {escape(name)}!"

@app.route("/path/<path:subpath>")
def subpath_route(subpath):
    return f'Subpath is {escape(subpath)}'

