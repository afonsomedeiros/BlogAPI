from bottle import Bottle

# from jwt_bottle import auth_required
from settings import API_VERSION

from app.action import category, subcategory


def create_category_route(app: Bottle):
    app.get(
        f"/{API_VERSION[-1]}/categories",
        callback=category.List,
        name="List all categories, could receive 'is_active' route param.",
    )

    app.get(
        f"/{API_VERSION[-1]}/category/<id:int>",
        callback=category.get,
        name="Get info about category."
    )

    app.post(
        f"/{API_VERSION[-1]}/category",
        callback=category.post,
        name="Create a new category."
    )

    app.put(
        f"/{API_VERSION[-1]}/category",
        callback=category.put,
        name="Update a category."
    )


def create_subcategory_route(app: Bottle):
    app.get(
        f"/{API_VERSION[-1]}/subcategories",
        callback=subcategory.List,
        name="List all subcategories, could receive 'is_active' route param.",
    )

    app.get(
        f"/{API_VERSION[-1]}/subcategory/<id:int>",
        callback=subcategory.get,
        name="Get info about subcategory."
    )

    app.post(
        f"/{API_VERSION[-1]}/subcategory",
        callback=subcategory.post,
        name="Create a new subcategory."
    )

    app.put(
        f"/{API_VERSION[-1]}/subcategory",
        callback=subcategory.put,
        name="Update a subcategory."
    )
