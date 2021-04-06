from marshmallow import fields, pre_dump
from marshmallow_peewee import ModelSchema
from .models import *


class UserSchema(ModelSchema):

    @pre_dump
    def replace_password(self, item, many, **kwargs):
        item.password = ""
        return item

    class Meta:
        model = User


class CategorySchema(ModelSchema):
    author = fields.Nested(UserSchema)

    class Meta:
        model = Category


class SubcategorySchema(ModelSchema):
    author = fields.Nested(UserSchema)
    category = fields.Nested(CategorySchema, only=[
                             'name', 'description', 'is_active'])

    class Meta:
        model = Subcategory


class PostSchema(ModelSchema):
    author = fields.Nested(UserSchema)
    subcategory = fields.Nested(SubcategorySchema, only=[
                                'name', 'description', 'is_active', 'category'])

    class Meta:
        model = Post


class CommentSchema(ModelSchema):
    class Meta:
        modela = Comment
