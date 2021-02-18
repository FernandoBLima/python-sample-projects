from dataclasses import dataclass

from marshmallow import Schema, fields


@dataclass(frozen=True)
class PokedexClass:
    Number: int
    Legend: bool
    Mega: bool
    Name: str
    Type_1: str
    Type_2: str
    Total: int
    HP: int
    Attack: int
    Defense: int
    SpAtk: int
    SpDef: int
    Speed: int
    Height: float
    Weight: float
    BMI: float
    Generation: int


class PokedexSchema(Schema):
    Number = fields.Integer(required=True)
    Legend = fields.Boolean(required=True)
    Mega: fields.Boolean(required=True)
    Name = fields.String(required=True)
    Type_1 = fields.String(required=True)
    Type_2 = fields.String(required=True)
    Total = fields.Integer(required=True)
    HP = fields.Integer(required=True)
    Attack = fields.Integer(required=True)
    Defense = fields.Integer(required=True)
    SpAtk = fields.Integer(required=True)
    SpDef = fields.Integer(required=True)
    Speed = fields.Integer(required=True)
    Height = fields.Float(required=True)
    Weight = fields.Float(required=True)
    BMI = fields.Float(required=True)
    Generation = fields.Integer(required=True)
