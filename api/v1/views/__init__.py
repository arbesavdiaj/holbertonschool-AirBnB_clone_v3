#!/usr/bin/python3
<<<<<<< HEAD
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places_amenities import *
=======
from flask import Blueprint
"""
Moudle to create Blueprint for our API
"""


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


from api.v1.views.states import *
from api.v1.views.index import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
>>>>>>> fa325c1a2eb0da37cf10643f5a3f032c7547be2a
