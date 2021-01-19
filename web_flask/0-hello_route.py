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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
