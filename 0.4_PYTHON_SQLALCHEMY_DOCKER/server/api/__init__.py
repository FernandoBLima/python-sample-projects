import logging

from aiohttp import web

from aiohttp_swagger import setup_swagger

from api.configuration.connect_db import DatabaseConnection
from api.enum import EnvironmentVariables
from api.routes import set_routes


def main():
    app = web.Application()

    connection = DatabaseConnection(
        db_name=EnvironmentVariables.NAME_DATABASE.get_env(),
        host=EnvironmentVariables.HOST_DATABASE.get_env(),
        username=EnvironmentVariables.USER_DATABASE.get_env(),
        password=EnvironmentVariables.PASSWORD_DATABASE.get_env(),
        port=EnvironmentVariables.PORT_DATABASE.get_env(),
    )
    engine_created = connection.create_database()
    logging.info('Connection created successful')
    session_created = connection.create_session(engine_created)

    set_routes(app)
    setup_swagger(app)
    app['session_db'] = session_created

    web.run_app(app, port=8000)
