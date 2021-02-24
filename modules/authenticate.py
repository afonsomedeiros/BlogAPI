from peewee import DoesNotExist

from app.models import User


class Auth(object):

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
    def get_user(obj_id: int):
        try:
            obj = User.get(User.id == obj_id)
            if obj:
                return obj
        except DoesNotExist as err:
            return {"error": f"User with id: {author_id} not exists."}