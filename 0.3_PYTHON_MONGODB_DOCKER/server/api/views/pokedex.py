
from aiohttp import web

from api.dataclasses.pokedex import PokedexClass, PokedexSchema
from api.models.pokedex import Pokedex

from marshmallow import Schema, fields

from webargs.aiohttpparser import use_args


class GetSchema(Schema):
    index = fields.Integer(required=False, default=None, missing=0)
    name = fields.String(required=False, default=None, missing='')
    hp = fields.Integer(required=False, default=None, missing=0)
    type1 = fields.String(required=False, default=None, missing='')
    type2 = fields.String(required=False, default=None, missing='')
    total = fields.Integer(required=False, default=None, missing=0)


class ResponseGetSchema(Schema):
    data = fields.List(
        fields.Nested(PokedexSchema),
        required=True
    )


class PokedexView(web.View):

    response = ResponseGetSchema()

    async def get(self):
        """
        ---
        description: This end-point allow to get some pokemon
        tags:
        - Pokedex
        produces:
        - text/plain
        responses:
        "200":
            description: successful operation. Return "pokemon" text
        """

        data = Pokedex.objects()
        resp = [
            PokedexClass(
                index=pokemon.index,
                Legend=pokemon.Legend,
                Mega=pokemon.Mega,
                Name=pokemon.Name,
                Type1=pokemon.Type1,
                Type2=pokemon.Type2,
                Total=pokemon.Total,
                HP=pokemon.HP,
                Attack=pokemon.Attack,
                Defense=pokemon.Defense,
                SpAtk=pokemon.SpAtk,
                SpDef=pokemon.SpDef,
                Speed=pokemon.Speed,
                Height=pokemon.Height,
                Weight=pokemon.Weight,
                BMI=pokemon.BMI,
                Generation=pokemon.Generation,
            )
            for pokemon in data]

        return web.json_response(self.response.dump(
            {
                'data': resp
            }
        ))


class PokedexFilterView(web.View):

    response = ResponseGetSchema()

    @use_args(GetSchema(), location="query")
    async def get(self, args):
        """
        ---
        description: This end-point allow to get some pokemon
        tags:
        - Pokedex
        responses:
        "200":
            description: successful operation. Return "pokemon" data
        """

        data = Pokedex.objects(
            Name__icontains=args["name"],
            Total__gte=args["total"],
            HP__gte=args["hp"],
            Type1__icontains=args["type1"],
            Type2__icontains=args["type2"],
        )

        resp = [
            PokedexClass(
                index=pokemon.index,
                Legend=pokemon.Legend,
                Mega=pokemon.Mega,
                Name=pokemon.Name,
                Type1=pokemon.Type1,
                Type2=pokemon.Type2,
                Total=pokemon.Total,
                HP=pokemon.HP,
                Attack=pokemon.Attack,
                Defense=pokemon.Defense,
                SpAtk=pokemon.SpAtk,
                SpDef=pokemon.SpDef,
                Speed=pokemon.Speed,
                Height=pokemon.Height,
                Weight=pokemon.Weight,
                BMI=pokemon.BMI,
                Generation=pokemon.Generation,
            )
            for pokemon in data]

        return web.json_response(self.response.dump(
            {
                'data': resp
            }
        ))
