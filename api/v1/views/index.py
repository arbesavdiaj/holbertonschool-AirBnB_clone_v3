#!/usr/bin/python3
<<<<<<< HEAD
""" Index """
from models.amenity import Amenity
=======
'''
Module to create the routes
for our api
'''
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
>>>>>>> fa325c1a2eb0da37cf10643f5a3f032c7547be2a
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
<<<<<<< HEAD
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
=======


@app_views.route("/status", strict_slashes=False)
def status():
    '''
    Status endpoint
    '''
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    '''
    Stats endpoint
    '''
    status = {}

    return jsonify({"amenities": storage.count(Amenity),
                    "cities": storage.count(City),
                    "places": storage.count(Place),
                    "reviews": storage.count(Review),
                    "states": storage.count(State),
                    "users": storage.count(User)})
>>>>>>> fa325c1a2eb0da37cf10643f5a3f032c7547be2a
