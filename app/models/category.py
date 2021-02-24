from peewee import CharField, BooleanField, ForeignKeyField

from data.engine import TimeStampBaseModel
from . import User


class Organize(TimeStampBaseModel):
    name = CharField(max_length=50)
    description = CharField(max_length=500)
    is_active = BooleanField(default=True)


class Category(Organize):
    author = ForeignKeyField(User)


class Subcategory(Organize):
    author = ForeignKeyField(User)
    category = ForeignKeyField(Category)