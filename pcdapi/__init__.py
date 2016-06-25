import os

from flask import Flask
from flask.ext.cors import CORS

from ce.views import add_routes

def get_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'CRMP_DSN', 'postgresql://httpd@monsoon.pcic.uvic.ca/crmp')
    add_routes(app)
    return app
