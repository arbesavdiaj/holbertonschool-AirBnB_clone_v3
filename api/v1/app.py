#!/usr/bin/python3
'''
Module to instatiate an flask app
to deploy our API
'''
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """Close storage on teardown."""
    storage.close()


if __name__ == "__main__":
    app.run(host=HBNB_API_HOST or '0.0.0.0',
            port=HBNB_API_PORT or 5000, threaded=True)
