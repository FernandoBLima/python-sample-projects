import logging

from app.enum import EnvironmentVariables
from app.producer import producer_api

from flask import Flask


app = Flask(__name__)

app.register_blueprint(producer_api, url_prefix='/producer')


@app.route('/')
def hello_world():
    env_variable = EnvironmentVariables.SERVICE.get_env()
    logging.info(f'enviroment variable: {env_variable}')
    return "Hello, World SERVER! " + env_variable


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
    )

    logging.info('Started Producer server...')

    app.run(
        host=EnvironmentVariables.SERVER_HOST.get_env(),
        port=EnvironmentVariables.SERVER_PORT.get_env(),
        debug=True
    )
