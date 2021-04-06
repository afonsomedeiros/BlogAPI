from bottle import request, response
from jwt_bottle import auth_required

from app.models import Category, User
from app.serializer import CategorySchema
from modules.DTO import transfer, get_info

import json


def List():
    page = int(request.query['page']) if 'page' in request.query else 1
    per_page = int(request.query['per_page']
                   ) if 'per_page' in request.query else 10
    if 'is_active' in request.query:
        data = Category.select().where(Category.is_active ==
                                       bool(request.query['is_active']))
    else:
        data = Category.select()
    obj, extra_fields = get_info(data, page, per_page)
    response.status = 200
    response.content_type = "Application/json"
    return json.dumps({
        'info': extra_fields,
        'categories': CategorySchema(many=True).dump(obj)
    })


def get(category_id):
    category = Category.get_by_id(category_id)
    category.author.password = ''
    response.status = 200
    response.content_type = "Application/json"
    return CategorySchema().dump(category)


@auth_required
def post(user: User):
    data = request.json
    obj: Category = transfer(data, Category)
    obj.author = user
    obj.save()
    response.status = 200
    response.content_type = "Application/json"
    return CategorySchema().dump(obj)


@auth_required
def put(user: User):
    data = request.json
    if 'id' not in data:
        return '{"message": "Data inválid."}'
    obj: Category = Category.get_by_id(data['id'])
    obj = transfer(data, Category, obj)
    obj.save()
    response.status = 200
    response.content_type = "Application/json"
    return CategorySchema().dump(obj)
