#!/usr/bin/python3
<<<<<<< HEAD
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """print web"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """print web"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """print C followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
=======
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 4eb5860b51c827a7ee115f26d1c9e6e64eb83b2b
