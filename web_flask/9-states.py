#!/usr/bin/python3

"""
Script that starts Flask web application.
The application listens on 0.0.0.0, port 5000.
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session.
    """
    storage.close()


@app.route("/states")
def states():
    """
    Renders html page with list of all State objects present in DBStorage.
    """
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route("/states/<id>")
def states_id(id=""):
    """
    If <id> is provided and exists, render html page with the State and \
    all its cities.
    """
    states = storage.all(State).values()
    return render_template("9-states.html", states=states, id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
