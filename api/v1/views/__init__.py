#!/usr/bin/python3
"""
This module contains endpoint(route) status
"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.amenities import *
