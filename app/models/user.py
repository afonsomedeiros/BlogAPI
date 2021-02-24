from data.engine import TimeStampBaseModel
from settings import SECRET

from peewee import CharField, DateField, IntegerField, DoesNotExist
from playhouse.signals import pre_save
from passlib.hash import pbkdf2_sha512 as hsh
from hashlib import md5

import datetime


class User(TimeStampBaseModel):
    """
        STATUS:
        0 - Admin
        1 - Author
        2 - Leitor
    """
    name: str = CharField(max_length=15)
    last_name: str = CharField(max_length=15, default="")
    social_name: str = CharField(max_length=30, null=True)
    status: int = IntegerField(default=2)
    email: str = CharField(max_length=100, unique=True)
    password: str = CharField(max_length=300)
    about_me: str = CharField(max_length=500, null=True)
    foto_path: str = CharField(max_length=500, null=True)
    birthday = DateField(null=True)

    def gen_hash(self):
        _secret = md5(SECRET.encode()).hexdigest()
        _password = md5(self.password.encode()).hexdigest()
        self.password = hsh.hash(_secret+_password)

    def verify(self, password):
        _secret = md5(SECRET.encode()).hexdigest()
        _password = md5(password.encode()).hexdigest()
        return hsh.verify(_secret+_password, self.password)

@pre_save(sender=User)
def before_save(models_class, instance: User, created):
    if type(instance.birthday) == str:
        instance.birthday = datetime.datetime.strptime(instance.birthday, "%Y-%m-%d")
            