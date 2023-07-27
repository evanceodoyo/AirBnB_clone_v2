#!/usr/bin/python3

"""
Script that starts Flask web application.
The application listens on 0.0.0.0, port 5000.
"""

from flask import Flask
from flask import render_template

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
    Replaces underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Defines /python/<text> route.
    Displays 'Python' followed by the value passed as <text>.
    Replaces underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Defines /number/<n> route.
    Displays '<n> is a number' only if <n> is an integer.
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Defines /number_template/<n> route.
    Display a HTML page only if <n> is an integer.
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Defines /number_odd_or_even/<n> route.
    Display a HTML only if <n> is an integer.
    In template, show if <n> is even or odd.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
