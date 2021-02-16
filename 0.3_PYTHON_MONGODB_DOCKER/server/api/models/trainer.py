from mongoengine import (
    Document,
    IntField,
    StringField,
)


class Trainers(Document):
    Name = StringField(max_length=200, required=True, unique=True)
    Region = StringField(max_length=200, required=True)
    Age = IntField(max_length=200, required=True)
