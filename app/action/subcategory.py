from app.models.category import Category
from bottle import request, response
from jwt_bottle import auth_required

from app.models import Subcategory, User
from app.serializer import SubcategorySchema
from modules.DTO import transfer

import json



def List():
    page = request.query['page'] if 'page' in request.query else 1
    per_page = request.query['per_page'] if 'per_page' in request.query else 10
    if 'is_active' in request.query:
        data = Subcategory.select().where(Subcategory.is_active == bool(request.query['is_active']))
    else:
        data = Subcategory.select()
    obj = data.paginate(page, per_page)
    for i in range(0, len(obj)): obj[i].author.password = ''
    total_pages = round(data.count())
    extra_fields ={
        "page": page,
        "per_page": obj.count(),
        "total": data.count(),
        "total_pages": total_pages if total_pages > 0 else 1,
    }
    categories = SubcategorySchema().dumps(obj)
    categories.append(extra_fields)
    response.status = 200
    response.content_type = "Application/json"
    return json.dumps(categories)


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

    