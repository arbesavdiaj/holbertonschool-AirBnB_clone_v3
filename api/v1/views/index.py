#!/usr/bin/python3
'''
Module to create the routes
for our api
'''
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", strict_slashes=False)
def status():
    '''
    Status endpoint
    '''
    return jsonify({"status": "OK"})
