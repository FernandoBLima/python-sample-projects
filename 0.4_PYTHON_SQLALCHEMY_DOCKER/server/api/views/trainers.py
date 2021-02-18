import logging

from aiohttp import web

from api.dataclasses.trainer import TrainerClass, TrainerSchema
from api.models.trainer import Trainers

from marshmallow import Schema, fields

from webargs.aiohttpparser import use_args


class GetSchema(Schema):
    name = fields.String(required=True)
    region = fields.String(required=False, default=None, missing='')
    age = fields.Integer(required=False, default=None, missing=0)


class ResponseGetSchema(Schema):
    data = fields.List(
        fields.Nested(TrainerSchema),
        required=True
    )


class TrainersView(web.View):

    response = ResponseGetSchema()

    async def get(self):
        """
        ---
        description: This end-point allow to get some trainers
        tags:
        - Trainer
        produces:
        - text/plain
        responses:
        "200":
            description: successful operation. Return "trainer" data
        """

        session = self.request.app['session_db']

        data = session.query(Trainers).all()
        resp = [
            TrainerClass(
                Name=trainer.name,
                Region=trainer.region,
                Age=trainer.age
            )
            for trainer in data]

        return web.json_response(self.response.dump(
            {
                'data': resp
            }
        ))

    @use_args(GetSchema(), location="query")
    async def post(self, args):
        """
        ---
        description: This end-point allow to save some strainer
        tags:
        - Trainer
        produces:
        - text/plain
        responses:
        "200":
            description: successful operation.
        """
        try:
            session = self.request.app['session_db']
            new_trainer = Trainers(
                name=args['name'],
                region=args['region'],
                age=args['age']
            )
            session.add(new_trainer)
            session.commit()
            logging.info('Saved successfully')

            return web.json_response({'message': 'Saved successfully'})

        except Exception as e:
            print(e)
            raise

    @use_args(GetSchema(), location="query")
    async def put(self, args):
        """
        ---
        description: This end-point allow to update some trainer
        tags:
        - Trainer
        produces:
        - text/plain
        responses:
        "200":
            description: successful operation.
        """
        try:
            session = self.request.app['session_db']

            update_trainer = session.query(Trainers).filter(
                Trainers.name == args["name"]).one()
            update_trainer.age = args["age"]
            session.commit()

            logging.info('Updated successfully')

            return web.json_response({'message': 'Updated successfully'})

        except Exception as e:
            print(e)
            raise

    @use_args(GetSchema(), location="query")
    async def delete(self, args):
        """
        ---
        description: This end-point allow to delete some trainer
        tags:
        - Trainer
        produces:
        - text/plain
        responses:
        "200":
            description: successful operation.
        """
        try:
            session = self.request.app['session_db']
            if args["name"]:
                looking_for = '%{0}%'.format(args["name"])
                session.query.filter_by(looking_for).delete()
                logging.info('Delete successfully')
                session.commit()

                return web.json_response({'message': 'Delete successfully'})

        except Exception as e:
            print(e)
            raise
