from dataclasses import dataclass

from marshmallow import Schema, fields


@dataclass(frozen=True)
class TrainerClass:
    Name: str
    Region: str
    Age: int


class TrainerSchema(Schema):
    Name = fields.String(required=True, unique=True)
    Region = fields.String(required=True)
    Age = fields.Integer(required=True)
