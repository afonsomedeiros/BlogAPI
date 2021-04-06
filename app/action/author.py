from bottle import request, response
from jwt_bottle import auth_required

from app.models import User
from app.serializer import UserSchema
from modules.DTO import transfer, get_info

import json


@auth_required
def get(user: User):
    """ Get logged author. """
    response.status = 200
    return UserSchema(exclude=["password"]).dump(user)


def perfil(id):
    obj = User.get_by_id(id)
    response.status = 200
    return UserSchema(exclude=["password"]).dump(obj)


def List():
    page = int(request.query["page"]) if "page" in request.query else 1
    per_page = int(request.query["per_page"]
                   ) if "per_page" in request.query else 10
    if "status" in request.query:
        data = User.select().where(User.status == request.query["status"])
    else:
        data = User.select()
    obj, extra_fields = get_info(data, page, per_page)
    response.status = 200
    response.content_type = "Application/json"
    return json.dumps({
        'info': extra_fields,
        'users': UserSchema(many=True).dump(obj)
    })


@auth_required
def post(user: User):
    if user.status == 0:
        data = request.json
        obj: User = transfer(data, User)
        obj.status = 1
        obj.gen_hash()
        obj.save()
        response.status = 201
        return UserSchema(exclude=["password"]).dump(obj)


def follower():
    data = request.json
    obj: User = transfer(data, User)
    obj.status = 2
    obj.gen_hash()
    obj.save()
    response.status = 201
    return UserSchema(exclude=["password"]).dump(obj)


@auth_required
def put(user: User):
    data = request.json
    obj: User = transfer(data, User, user)
    obj.status = user.status
    obj.save()
    response.status = 200
    return UserSchema(exclude=["password"]).dump(obj)
