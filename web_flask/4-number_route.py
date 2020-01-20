#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)

app.route('/')


@app.route("/", strict_slashes=False)
def print():
    """Return a string"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def print_2():
    """Return a string"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def print_c(text):
    """print  a directory"""
    aux_text = text.replace('_', ' ')
    return "C {}".format(aux_text)


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>")
def print_python(text):
    """display “Python ”, followed by the value
    of the text variable
    (replace underscore _ symbols with a space"""
    aux_text = text.replace('_', ' ')
    return "Python {}".format(aux_text)


@app.route("/number/<int:n>", strict_slashes=False)
def print_number(n):
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run()
