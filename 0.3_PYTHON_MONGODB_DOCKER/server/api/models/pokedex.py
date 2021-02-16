from mongoengine import (
    BooleanField,
    Document,
    FloatField,
    IntField,
    StringField,
)


class Pokedex(Document):
    index = StringField()
    Legend = BooleanField()
    Mega = BooleanField()
    Name = StringField()
    Type1 = StringField()
    Type2 = StringField()
    Total = IntField()
    HP = IntField()
    Attack = IntField()
    Defense = IntField()
    SpAtk = IntField()
    SpDef = IntField()
    Speed = IntField()
    Height = FloatField()
    Weight = FloatField()
    BMI = IntField()
    Generation = IntField()
