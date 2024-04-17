#!/usr/bin/python3
'''
Module to instatiate an flask app
to deploy our API
'''
from flask import Flask
from os import getenv
from models import storage
from api.v1.views import app_views


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Method to handle app teardown.
    """
    storage.close()


if __name__ == "__main__":
    '''
    Starting server
    '''
    app.run(host=getenv("HBNB_API_HOST", default="0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", default=5000)),
            threaded=True)
