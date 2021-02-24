from bottle import Bottle

from settings import API_VERSION

from app.models import Post
from app.action import post


def create_posts_routes(app: Bottle):
    """
        Type get routes: 
            sub -> filter by subcategory.
            con -> filter by content in title, description and content.
            aut -> filter by Author.
            las -> Get last posts.

        Types route params:
            page: number of page.
            per_page: results per page.
            query: if type equals 'sub', 'con' or 'aut' should pass a query page.
    """
    app.get(f'/{API_VERSION[-1]}/posts/<t>', callback=post.List, name="""
        Type get routes: 
            sub -> filter by subcategory.
            con -> filter by content in title, description and content.
            aut -> filter by Author.
            las -> Get last posts.

        Types route params:
            page: number of page.
            per_page: results per page.
            query: if type equals 'sub', 'con' or 'aut' should pass a query page.
    """)