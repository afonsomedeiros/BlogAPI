from jwt_bottle import JWTPlugin
from bottle import Bottle
from settings import JWT_SECRET
from modules.authenticate import Auth


def install_user(app: Bottle):
    jwt = JWTPlugin(JWT_SECRET, Auth)
    app.install(jwt)