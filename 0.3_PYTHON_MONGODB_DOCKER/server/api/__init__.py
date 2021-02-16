import logging

from aiohttp import web

from aiohttp_swagger import setup_swagger

from api.configuration.mongo import MongoConnection
from api.enum import EnvironmentVariables
from api.routes import set_routes

from dotenv import load_dotenv


def main():
    try:
        load_dotenv()

        app = web.Application()
        connection = MongoConnection(
            db_name=EnvironmentVariables.NAME_DATABASE.get_env(),
            host=EnvironmentVariables.HOST_DATABASE.get_env(),
            port=EnvironmentVariables.PORT_DATABASE.get_env(),
            username='',
            password=''
        )
        connection.create_database()
        logging.info('Connection successful')
        set_routes(app)
        setup_swagger(app)

        web.run_app(app, port=8000)

    except Exception as e:
        logging.info('Connection successful', e)
