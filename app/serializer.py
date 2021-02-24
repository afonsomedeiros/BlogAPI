from marshmallow_peewee import ModelSchema
from .models import *


class UserSchema(ModelSchema):
    class Meta:
        model = User


class CategorySchema(ModelSchema):
    class Meta:
        model = Category


class SubcategorySchema(ModelSchema):
    class Meta:
        model = Subcategory


class PostSchema(ModelSchema):
    class Meta:
        model = Post


class CommentSchema(ModelSchema):
    class Meta:
        modela = Comment