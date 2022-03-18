from flask_mongoengine import MongoEngine
from mongoengine import *
from mongoengine.connection import connect
from mongoengine.fields import *
from mongoengine.document import *

connect("DB1")
class User(DynamicDocument):
    name = StringField()
    email = EmailField()
    Id = StringField()
    Question = StringField()
