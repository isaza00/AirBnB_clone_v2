#!/usr/bin/python3
"""  starts a Flask web application """

from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)

"""
def get_db():
    """ get db """
    if 'db' not in g:
        g.db = storage
    return g.db

@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)
    if db is not None:
        storage.close()
"""

@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays list of states"""
    dic = {}
    final = {}
    for key, value in storage.all(State).items():
        dic[key] = value.to_dict()
    print(dic)
    for key, value in dic.items():
        final[value["name"]] = value["id"]
    print(final)

    return render_template('7-states_list.html', dic=final)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
