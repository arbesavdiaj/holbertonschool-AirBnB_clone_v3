#!/usr/bin/python3
'''
Module to create the routes
for our api
'''
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """
    Route to return the status.
    """
    return jsonify({"status": "OK"})
