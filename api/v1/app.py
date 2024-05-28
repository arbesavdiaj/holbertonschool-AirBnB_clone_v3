#!/usr/bin/python3
<<<<<<< HEAD
""" Flask Application """
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
=======
'''
Module to instatiate an flask app
to deploy our API
'''
from flask import Flask
from models import storage
from os import getenv
from flask import jsonify
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=['0.0.0.0'])
app.register_blueprint(app_views)


@app.errorhandler(404)
def error_404(error):
    return jsonify({"error": "Not found"}), 404
>>>>>>> fa325c1a2eb0da37cf10643f5a3f032c7547be2a


@app.teardown_appcontext
def close_db(error):
<<<<<<< HEAD
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
=======
    '''
    Function call to close db connection
    after each app teardwon
    '''
    storage.close()


if __name__ == "__main__":
    '''
    Starting server
    '''
    app.run(host=getenv("HBNB_API_HOST", default="0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", default=5000)),
            threaded=True)
>>>>>>> fa325c1a2eb0da37cf10643f5a3f032c7547be2a
