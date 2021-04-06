from app.models.category import Category
from bottle import request, response
from jwt_bottle import auth_required

from app.models import Subcategory, User
from app.serializer import SubcategorySchema
from modules.DTO import transfer, get_info

import json


def List():
    page = request.query['page'] if 'page' in request.query else 1
    per_page = request.query['per_page'] if 'per_page' in request.query else 10
    if 'is_active' in request.query:
        data = Subcategory.select().where(Subcategory.is_active ==
                                          bool(request.query['is_active']))
    else:
        data = Subcategory.select()
    obj, extra_fields = get_info(data, page, per_page)
    response.status = 200
    response.content_type = "Application/json"
    return json.dumps({
        'info': extra_fields,
        'subcategories': SubcategorySchema(many=True).dump(obj)
    })


def get(subcategory_id):
    Subcategory = Subcategory.get_by_id(subcategory_id)
    Subcategory.author.password = ''
    response.status = 200
    response.content_type = "Application/json"
    return SubcategorySchema().dump(Subcategory)


@auth_required
def post(user: User):
    data = request.json
    obj: Subcategory = transfer(data, Subcategory)
    obj.author = user
    obj.category = Category.get_by_id(data['category_id'])
    obj.save()
    response.status = 200
    response.content_type = "Application/json"
    return SubcategorySchema().dump(obj)


@auth_required
def put(user: User):
    data = request.json
    if 'id' not in data:
        return '{"message": "Data inválid."}'
    obj: Subcategory = Subcategory.get_by_id(data['id'])
    obj = transfer(data, Subcategory, obj)
    obj.save()
    response.status = 200
    response.content_type = "Application/json"
    return SubcategorySchema().dump(obj)
