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


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Renders html page with list of all City objects by State objects present \
    in DBStorage.
    """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
