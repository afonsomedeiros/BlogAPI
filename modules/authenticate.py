from peewee import DoesNotExist
from jwt_bottle import BaseAuth

from app.models import User


class Auth(BaseAuth):

    @staticmethod
    def authenticate(*args, **kwargs):
        try:
            if "email" in kwargs and "password" in kwargs:
                obj = User.get(User.email == kwargs['email'])
                if obj and obj.verify(kwargs['password']):
                    return obj
            return None
        except DoesNotExist as err:
            return {"error": f"User {kwargs['email']} not exists."}

    @staticmethod
    def get_user(*args, **kwargs):
        try:
            obj = User.get(User.id == kwargs['id'])
            if obj:
                return obj
        except DoesNotExist as err:
            return {"error": f"User with id: {kwargs['id']} not exists."}
