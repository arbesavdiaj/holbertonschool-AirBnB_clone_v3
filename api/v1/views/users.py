#!/usr/bin/python3
<<<<<<< HEAD
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_users():
    """
    Retrieves the list of all user objects
    or a specific user
    """
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_user(user_id):
    """ Retrieves an user """
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a user Object
    """

    user = storage.get(User, user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_user():
    """
    Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_user(user_id):
    """
    Updates a user
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
=======
'''
Modul to create API endpoints
'''
from models import storage
from models.user import User
from flask import jsonify
from flask import request
from api.v1.views import app_views
from flask import abort


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
@app_views.route('/users/<user_id>',
                 methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def return_users(user_id=None):
    '''
    Status endpoint
    '''

    if request.method == 'GET':
        if user_id is None:
            users = []
            for obj in storage.all(User).values():
                users.append(obj.to_dict())
            return jsonify(users)
        user = storage.get(User, user_id)
        if user is None:
            return abort(404)
        return jsonify(user.to_dict())
    if request.method == 'PUT':
        user = storage.get(User, user_id)
        if user is None:
            return abort(404)
        data = request.get_json(force=True)
        if not data:
            return abort(400, description="Not a JSON")
        for k, v in data.items():
            if k not in ['id', 'updated_at', 'created_at', 'email']:
                setattr(user, k, data[k])
        storage.save()
        return jsonify(user.to_dict())
    if request.method == 'DELETE':
        if user_id is None:
            return abort(404)
        obj = storage.get(User, user_id)
        if obj is None:
            return abort(404)
        storage.delete(obj)
        storage.save()
        return jsonify({}), 200
    if request.method == 'POST':
        data = request.get_json(silent=True, force=True)
        if not data:
            return abort(400, description="Not a JSON")
        user_email = data.get("email", None)
        user_password = data.get("password", None)
        if user_email is None:
            return abort(400, description="Missing email")
        if user_password is None:
            return abort(400, description="Missing password")
        new_user = User(email=user_email, password=user_password)
        storage.new(new_user)
        storage.save()
        return jsonify(new_user.to_dict()), 201
>>>>>>> fa325c1a2eb0da37cf10643f5a3f032c7547be2a
