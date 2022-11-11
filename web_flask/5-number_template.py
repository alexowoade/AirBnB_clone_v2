#!/usr/bin/python3
""" A script that starts a flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ displays 'C' followed  by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ displays 'Python' followed  by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """ display 'n is a number' only if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    """ display a HTML page only if n is an integer """
    return '<!DOCTYPE html>\n\
<HTML lang="en">\n\
\t<HEAD>\n\
\t\t<TITLE>HBNB</TITLE>\n\
\t</HEAD>\n\
\t<BODY>\n\
\t\t<H1>Number: 89</H1>\n\
\t</BODY>\n\
</HTML>'.format(n)


if __name__ == "__main__":
    """ run flask web app """
    app.run(host='0.0.0.0', port=5000)
