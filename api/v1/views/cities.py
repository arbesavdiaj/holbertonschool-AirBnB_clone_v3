#!/usr/bin/python3
<<<<<<< HEAD
""" objects that handles all default RestFul API actions for cities """
from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/city/cities_by_state.yml', methods=['GET'])
def get_cities(state_id):
    """
    Retrieves the list of all cities objects
    of a specific State, or a specific city
    """
    list_cities = []
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    for city in state.cities:
        list_cities.append(city.to_dict())

    return jsonify(list_cities)


@app_views.route('/cities/<city_id>/', methods=['GET'], strict_slashes=False)
@swag_from('documentation/city/get_city.yml', methods=['GET'])
def get_city(city_id):
    """
    Retrieves a specific city based on id
    """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/city/delete_city.yml', methods=['DELETE'])
def delete_city(city_id):
    """
    Deletes a city based on id provided
    """
    city = storage.get(City, city_id)

    if not city:
        abort(404)
    storage.delete(city)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/city/post_city.yml', methods=['POST'])
def post_city(state_id):
    """
    Creates a City
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = City(**data)
    instance.state_id = state.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/city/put_city.yml', methods=['PUT'])
def put_city(city_id):
    """
    Updates a City
    """
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'state_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(city, key, value)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
=======
'''
Modul to create API endpoints
'''
from models import storage
from models.state import State
from models.city import City
from flask import jsonify
from flask import request
from api.v1.views import app_views
from flask import abort


@app_views.route('/states/<state_id>/cities',
                 methods=['GET', 'POST'], strict_slashes=False)
def get_cities(state_id=None):
    '''
    Simple route
    '''
    state = storage.get(State, state_id)
    if state is None:
        return abort(404)
    if request.method == 'GET':
        cities = [city.to_dict() for city in state.cities]
        return jsonify(cities)
    if request.method == 'POST':
        data = request.get_json(silent=True, force=True)
        if not data:
            return abort(400, description="Not a JSON")
        city_name = data.get("name", None)
        if city_name is None:
            return abort(400, description="Missing name")
        new_city = City(name=city_name, state_id=state_id)
        storage.new(new_city)
        storage.save()
        return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>',
                 methods=['DELETE', 'GET', 'PUT'], strict_slashes=False)
def delete_city(city_id=None):
    '''
    Simple route
    '''
    city = storage.get(City, city_id)
    if city is None:
        return abort(404)
    if request.method == 'DELETE':
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    if request.method == 'GET':
        return jsonify(city.to_dict()), 200
    if request.method == 'PUT':
        data = request.get_json(force=True)
        if not data:
            return abort(400, description="Not a JSON")
        for k, v in data.items():
            if k not in ['id', 'updated_at', 'created_at', 'state_id']:
                setattr(city, k, data[k])
        storage.save()
        return jsonify(city.to_dict()), 200
>>>>>>> fa325c1a2eb0da37cf10643f5a3f032c7547be2a
