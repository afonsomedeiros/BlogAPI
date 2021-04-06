from peewee import TextField, CharField, BooleanField, IntegerField, ForeignKeyField

from data.engine import TimeStampBaseModel
from . import Subcategory, User


class Post(TimeStampBaseModel):
    """
        status
        0 - Rascunho.
        1 - Publicado.
        2 - Inativo.
    """
    title = CharField(max_length=100, default="Nova Postagem")
    description = CharField(max_length=300, null=True)
    content = TextField()
    status = IntegerField(default=0)
    image = CharField(max_length=300, null=True)
    author = ForeignKeyField(User)
    subcategory = ForeignKeyField(Subcategory)


class Comment(TimeStampBaseModel):
    user = ForeignKeyField(User)
    post = ForeignKeyField(Post)
    content = CharField(max_length=1000)
    status = BooleanField(default=False)
