from flask import Blueprint

from .enum import EnvironmentVariables
from .rabbitmq import RabbitMQ
from .rabbitmq import RabbitMQConfigure

producer_api = Blueprint('producer_api', __name__)


@producer_api.route('/add/<body>')
def publish_message(body):
    server = RabbitMQConfigure(
        queue=EnvironmentVariables.RABBITMQ_QUEUE.get_env(),
        host=EnvironmentVariables.RABBITMQ_HOST.get_env(),
        routing_key=EnvironmentVariables.RABBITMQ_ROUTING_KEY.get_env(),
        exchange=''
    )

    rabbitmq = RabbitMQ(server)
    rabbitmq.publish(message={"data": body})
    return " [x] Body sent: %s" % body
