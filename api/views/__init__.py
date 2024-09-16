#!/usr/bin/python3
"""Blueprint for the API"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/')

from api.views.concepts import *
from api.views.index import *