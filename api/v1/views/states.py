#!/usr/bin/python3
"""
Create a new view for State objects that handles
all default RESTFul API actions:
"""


from flask import jsonify, request
from api.v1.views import app_views
from models import State


@app_views.route('/states', methods=['GET'])
def get_states():
    """function to get all states"""
    states = State.query.all()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """function to get state"""
    state = State.query.get(state_id)
    if state:
        return jsonify(state.to_dict())
    else:
        return jsonify({'error': 'State not found'}), 404


@app_views.route('/states', methods=['POST'])
def create_state():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Missing name parameter'}), 400
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """function to update a state"""
    state = State.query.get(state_id)
    if state:
        data = request.get_json()
        for key, value in data.items():
            setattr(state, key, value)
        state.save()
        return jsonify(state.to_dict())
    else:
        return jsonify({'error': 'State not found'}), 404


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """function to delete a state"""
    state = State.query.get(state_id)
    if state:
        state.delete()
        return jsonify({'message': 'State deleted successfully'})
    else:
        return jsonify({'error': 'State not found'}), 404
