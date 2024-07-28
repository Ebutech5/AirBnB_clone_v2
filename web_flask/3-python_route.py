#!/usr/bin/python3
'''
    Start a flask web application
'''
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Return Hello HBNB!"""
    return 'Hello HBNB!'
@app.route('/hbnb', strict_slashes=False)
def index():
    """Return HBNB"""
    return 'HBNB'
@app.route('/c/<text>', strict_slashes=False)
def index(text):
    """Display "c" followed by value of text variable"""
    return 'c' + text.replace('_', '')
@app.route('/python/' defaults={'text': 'is cool'})
@app.route('/python/<text>' strict_slashes=False)
def index(text):
    """Display "Python" followed by value of text variable"""
    return 'Python' + text.replace('_', '')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)