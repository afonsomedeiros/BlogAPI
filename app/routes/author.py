from bottle import Bottle

# from jwt_bottle import auth_required
from settings import API_VERSION

from app.action import author


def create_author_route(app: Bottle):
    app.get(
        f"/{API_VERSION[-1]}/author",
        callback=author.get,
        name="Get data from authenticated author.",
    )

    app.get(f'/{API_VERSION[-1]}/author/list', callback=author.List, name="Get list data.")

    app.get(f'/{API_VERSION[-1]}/author/<id>', callback=author.perfil, name="Get data from another Author.")


    app.post(
        f"/{API_VERSION[-1]}/author", callback=author.post, name="Create new Author."
    )

    app.put(
        f"/{API_VERSION[-1]}/author", callback=author.put, name="update new author."
    )
