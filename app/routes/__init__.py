from operator import pos
from bottle import Bottle

from . import author
from . import category
from . import post
from . import spec

def create_routes(app: Bottle):
    author.create_author_route(app)
    category.create_category_route(app)
    category.create_subcategory_route(app)
    post.create_posts_routes(app)
    spec.create_spec_route(app)