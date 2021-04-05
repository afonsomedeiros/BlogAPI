from jwt_bottle import JWTPlugin
from bottle import Bottle
from settings import JWT_SECRET
from modules.authenticate import Auth


def install_user(app: Bottle):
    configs = [
        {
            'model': Auth,
            'endpoint': '/auth',
            'auth_name': "auth",
            'refresh_name': 'refresh'
        }
    ]
    jwt = JWTPlugin(JWT_SECRET, configs, payload=['id', 'status'])
    app.install(jwt)
