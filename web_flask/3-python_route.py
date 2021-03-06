#!/usr/bin/python3
"""Script that starts a Flask web application listening on 0.0.0.0, port 5000,
Routes: "/: display “Hello HBNB!”"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """method, this will be the one in charge of controlling the requests or
    Requests that arrive on the route and of returning the content through a
    Response."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_world2():
    """method, this will be the one in charge of controlling the requests or
    Requests that arrive on the route and of returning the content through a
    Response."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text=""):
    """Display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text=""):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
