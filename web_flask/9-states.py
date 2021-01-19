#!/usr/bin/python3
"""Script that fetches data from the storage engine """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', defaults={'id': None}, strict_slashes=False)
def states_li2(id):
    """list of all State objects present in DBStorage with the id"""
    states = storage.all(State)
    if id:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
