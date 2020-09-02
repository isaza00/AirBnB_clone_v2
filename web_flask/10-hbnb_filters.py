#!/usr/bin/python3
"""  starts a Flask web application """

from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    """ displays list of cities by states"""
    
    return render_template('10-hbnb_filters.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)