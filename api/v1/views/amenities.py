#!/usr/bin/python3
<<<<<<< HEAD
""" objects that handles all default RestFul API actions for Amenities"""
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
@swag_from('documentation/amenity/all_amenities.yml')
def get_amenities():
    """
    Retrieves a list of all amenities
    """
    all_amenities = storage.all(Amenity).values()
    list_amenities = []
    for amenity in all_amenities:
        list_amenities.append(amenity.to_dict())
    return jsonify(list_amenities)


@app_views.route('/amenities/<amenity_id>/', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/amenity/get_amenity.yml', methods=['GET'])
def get_amenity(amenity_id):
    """ Retrieves an amenity """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/amenity/delete_amenity.yml', methods=['DELETE'])
def delete_amenity(amenity_id):
    """
    Deletes an amenity  Object
    """

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    storage.delete(amenity)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
@swag_from('documentation/amenity/post_amenity.yml', methods=['POST'])
def post_amenity():
    """
    Creates an amenity
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Amenity(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/amenity/put_amenity.yml', methods=['PUT'])
def put_amenity(amenity_id):
    """
    Updates an amenity
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(amenity, key, value)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 200)
=======
'''
Modul to create API endpoints
'''
from models import storage
from models.amenity import Amenity
from flask import jsonify
from flask import request
from api.v1.views import app_views
from flask import abort


@app_views.route('/amenities', methods=['GET', 'POST'], strict_slashes=False)
@app_views.route('/amenities/<amenity_id>',
                 methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def return_amenities(amenity_id=None):
    '''
    Status endpoint
    '''

    if request.method == 'GET':
        if amenity_id is None:
            amenities = []
            for obj in storage.all(Amenity).values():
                amenities.append(obj.to_dict())
            return jsonify(amenities)
        amenitiy = storage.get(Amenity, amenity_id)
        if amenitiy is None:
            return abort(404)
        return jsonify(amenitiy.to_dict())
    if request.method == 'PUT':
        amenity = storage.get(Amenity, amenity_id)
        if amenity is None:
            return abort(404)
        data = request.get_json(force=True)
        if not data:
            return abort(400, description="Not a JSON")
        for k, v in data.items():
            if k not in ['id', 'updated_at', 'created_at']:
                setattr(amenity, k, data[k])
        storage.save()
        return jsonify(amenity.to_dict())
    if request.method == 'DELETE':
        if amenity_id is None:
            return abort(404)
        obj = storage.get(Amenity, amenity_id)
        if obj is None:
            return abort(404)
        storage.delete(obj)
        storage.save()
        return jsonify({}), 200
    if request.method == 'POST':
        data = request.get_json(silent=True, force=True)
        if not data:
            return abort(400, description="Not a JSON")
        amenity_name = data.get("name", None)
        if amenity_name is None:
            return abort(400, description="Missing name")
        new_amenity = Amenity(name=amenity_name)
        storage.new(new_amenity)
        storage.save()
        return jsonify(new_amenity.to_dict()), 201
>>>>>>> fa325c1a2eb0da37cf10643f5a3f032c7547be2a
