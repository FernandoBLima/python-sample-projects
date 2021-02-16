from dataclasses import dataclass

from marshmallow import Schema, fields


@dataclass(frozen=True)
class PokedexClass:
    index: int
    Legend: bool
    Mega: bool
    Name: str
    Type1: str
    Type2: str
    Total: int
    HP: int
    Attack: int
    Defense: int
    SpAtk: int
    SpDef: int
    Speed: int
    Height: int
    Weight: int
    BMI: str
    Generation: int


class PokedexSchema(Schema):
    index = fields.Integer(required=True)
    Legend = fields.Boolean(required=True)
    Mega: fields.Boolean(required=True)
    Name = fields.String(required=True)
    Type1 = fields.String(required=True)
    Type2 = fields.String(required=True)
    Total = fields.Integer(required=True)
    HP = fields.Integer(required=True)
    Attack = fields.Integer(required=True)
    Defense = fields.Integer(required=True)
    SpAtk = fields.Integer(required=True)
    SpDef = fields.Integer(required=True)
    Speed = fields.Integer(required=True)
    Height = fields.Integer(required=True)
    Weight = fields.Integer(required=True)
    BMI = fields.String(required=True)
    Generation = fields.Integer(required=True)
