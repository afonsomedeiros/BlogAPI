from bottle import Bottle
from settings import API_VERSION
from .extension import jwt

from .routes import create_routes


def createa_admin_app():
    app = Bottle()

    return app


def create_app():
    app = Bottle()

    create_routes(app)
    jwt.install_user(app)

    app.merge(createa_admin_app())

    return app