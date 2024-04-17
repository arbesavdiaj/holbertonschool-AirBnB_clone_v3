#!/usr/bin/python3
'''
Module to instatiate an flask app
to deploy our API
'''
from flask import Flask
import os
from models import storage
from api.v1.views import app_views


app = Flask(__name__)  # Creating an instance of Flask


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Method to handle app teardown.
    """
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
