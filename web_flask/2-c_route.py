#!/usr/bin/python3

"""
Script that starts Flask web application.
The application listens on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Defines the home or index route.
    Displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Defines hbnb route.
    Displays 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Defines /c/<text> (dynamic) route.
    Displays 'C' followed by the value passed as <text>.
    """
    text = text.replace("_", " ")
    return "C {}". format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
