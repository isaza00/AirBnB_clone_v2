#!/usr/bin/python3
"""  starts a Flask web application """

from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)

"""
def get_db():
    
    if 'db' not in g:
        g.db = storage
    return g.db

@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)
    if db is not None:
        storage.close()
"""

@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ displays list of cities by states"""
    dic = {}
    states = {}
    for key, value in storage.all(State).items():
        dic[key] = value.to_dict()
        print("VALUE:", value.name)
    for key, value in dic.items():
        states[value["name"]] = value["id"]
    return render_template('7-states_list.html', dic=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
