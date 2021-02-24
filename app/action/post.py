from app.action.category import post
from operator import truediv
from bottle import request, response
from jwt_bottle import auth_required

from app.models import Subcategory, User, Post
from app.serializer import PostSchema
from modules.DTO import transfer, get_info

import json


def get_last_posts(escape: str, page: int = 1, per_page: int = 10):
    """ Only with status 1. """
    data = Post.select().where(Post.status == 1)
    return get_info(data, page, per_page)


def get_by_subcategory(subcategory_id: int, page: int = 1, per_page: int = 10):
    """ Only with status 1. """
    data = Post.select().where(
        (Post.subcategory == Subcategory.get_by_id(subcategory_id)) & (Post.status == 1)
    )
    return get_info(data, page, per_page)


def get_by_content(content: str, page: int = 1, per_page: int = 10):
    """ Only with status 1. """
    data = Post.select().where(
        (Post.title % f"%{content}%")
        | (Post.description % f"%{content}%")
        | (Post.content % f"%{content}%") & (Post.status == 1)
    )
    return get_info(data, page, per_page)


def get_by_author(author_id: int, page: int = 1, per_page: int = 10):
    """ Only with status 1. """
    data = Post.select().where(
        (Post.author == User.get_by_id(author_id)) & (Post.status == 1)
    )
    return


def List(t: str):
    func = {
        "sub": get_by_subcategory,
        "con": get_by_content,
        "aut": get_by_author,
        "las": get_last_posts,
    }
    page = int(request.query["page"]) if "page" in request.query else 1
    per_page = int(request.query["per_page"]) if "per_page" in request.query else 10
    query = request.query["query"] if "query" in request.query else ""
    obj, extra_fields = func[t](query, page, per_page)
    for i in range(0, len(obj)):
        obj[i].author.password = ""
    posts = PostSchema(many=True).dump(obj)
    posts.append(extra_fields)
    response.status = 200
    response.content_type = "Application/json"
    return json.dumps(posts)


def get(post_id):
    post = Post.get_by_id(post_id)
    post.author.password = ""
    schema = PostSchema().dump(post)
    response.status = 200
    response.content_type = "Application/json"
    return schema


@auth_required
def post(user: User):
    data = request.json
    post: Post = transfer(data, Post)
    post.subcategory = Subcategory.get_by_id(data["subcategory_id"])
    post.author = user
    post.save()
    post.author.password = ""
    schema = PostSchema().dump(post)
    response.status = 200
    response.content_type = "Application/json"
    return schema


@auth_required
def put(user: User):
    data = request.json
    if "id" not in data:
        return '{"message": "Data inválid."}'
    obj: Post = Post.get_by_id(data["id"])
    obj = transfer(data, Post, obj)
    obj.save()
    response.status = 200
    response.content_type = "Application/json"
    return PostSchema().dump(obj)
