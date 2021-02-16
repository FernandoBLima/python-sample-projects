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

        data = Trainers.objects()
        resp = [
            TrainerClass(
                Name=trainer.Name,
                Region=trainer.Region,
                Age=trainer.Age
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
            new_trainer = Trainers(
                Name=args['name'],
                Region=args['region'],
                Age=args['age']
            )
            new_trainer.save()
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
            update_trainer = Trainers.objects(
                Name__icontains=args["name"]
            )
            update_trainer.update(Age=args['age'])
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
            delete_trainer = Trainers.objects(
                Name__icontains=args["name"]
            )
            delete_trainer.delete()
            logging.info('Delete successfully')

            return web.json_response({'message': 'Delete successfully'})

        except Exception as e:
            print(e)
            raise
