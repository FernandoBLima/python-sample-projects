from aiohttp import web

from api.dataclasses.pokedex import PokedexClass, PokedexSchema
from api.models.pokedex import Pokedex

from marshmallow import Schema, fields

from webargs.aiohttpparser import use_kwargs


class GetSchema(Schema):
    # index = fields.Integer(required=False, default=None, missing=0)
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
            description: successful operation. Return "Pokedex" text
        """

        session = self.request.app['session_db']

        data = session.query(Pokedex).all()
        resp = [
            PokedexClass(
                Number=pokemon.number,
                Legend=pokemon.legend,
                Mega=pokemon.mega,
                Name=pokemon.name,
                Type_1=pokemon.type_1,
                Type_2=pokemon.type_2,
                Total=pokemon.total,
                HP=pokemon.hp,
                Attack=pokemon.attack,
                Defense=pokemon.defense,
                SpAtk=pokemon.spatk,
                SpDef=pokemon.spdef,
                Speed=pokemon.speed,
                Height=pokemon.height,
                Weight=pokemon.weight,
                BMI=pokemon.bmi,
                Generation=pokemon.generation,
            )
            for pokemon in data]

        return web.json_response(self.response.dump(
            {
                'data': resp
            }
        ))


class PokedexFilterView(web.View):

    response = ResponseGetSchema()

    @use_kwargs(GetSchema(), location="query")
    async def get(self, name, hp, type1, type2, total):
        """
        ---
        description: This end-point allow to get some pokemon
        tags:
        - Pokedex
        responses:
        "200":
            description: successful operation. Return "pokemon" data
        """

        session = self.request.app['session_db']
        query = session.query(Pokedex)

        if name:
            looking_for = '%{0}%'.format(name)
            query = query.filter(Pokedex.name.ilike(looking_for))

        if hp:
            query = query.filter(Pokedex.hp >= hp)

        if type1:
            looking_for = '%{0}%'.format(type1)
            query = query.filter(Pokedex.type1.ilike(looking_for))

        if type2:
            looking_for = '%{0}%'.format(type2)
            query = query.filter(Pokedex.type2.ilike(looking_for))

        if total:
            query = query.filter(Pokedex.total >= total)

        resp = [
            PokedexClass(
                Number=pokemon.number,
                Legend=pokemon.legend,
                Mega=pokemon.mega,
                Name=pokemon.name,
                Type_1=pokemon.type_1,
                Type_2=pokemon.type_2,
                Total=pokemon.total,
                HP=pokemon.hp,
                Attack=pokemon.attack,
                Defense=pokemon.defense,
                SpAtk=pokemon.spatk,
                SpDef=pokemon.spdef,
                Speed=pokemon.speed,
                Height=pokemon.height,
                Weight=pokemon.weight,
                BMI=pokemon.bmi,
                Generation=pokemon.generation,
            )
            for pokemon in query]

        return web.json_response(self.response.dump(
            {
                'data': resp
            }
        ))


class PokedexWelcome(web.View):

    async def get(self):
        return web.json_response({
            'message': 'Hello World!'
        })
