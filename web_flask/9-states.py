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


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=""):
    """
    Renders html page with list of all State objects present in DBStorage.
    If <id> is provided and exists, render html page with the State and \
    all its cities.
    """
    states = []
    states_objs = storage.all(State).values()

    if id:
        for state_obj in states_objs:
            if id == state_obj.id:
                states.append(state_obj)
    else:
        states.extend(states_objs)
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
