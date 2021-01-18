import logging

from app.enum import EnvironmentVariables

import pika


class RabbitMQConfigure():

    def __init__(self, queue, host, routing_key, exchange=''):
        """
        Configure RabbitMQ Server

        :param queue: buffer that stores messages.
        :param host: Which the underlying TCP connection is made
        :param routing_key:
        :param exchange:

        """
        self.queue = queue
        self.host = host
        self.routing_key = routing_key
        self.exchange = exchange


class RabbitMQ():

    def __init__(self, server):
        """
        :param server: Object of RabbitmqConfigure
        """

        self.server = server

        credentials = pika.PlainCredentials(
            EnvironmentVariables.RABBITMQ_USER_DEFAULT.get_env(),
            EnvironmentVariables.RABBITMQ_PASS_DEFAULT.get_env(),
        )
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                self.server.host,
                credentials=credentials
            ))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue, durable=False)

    def publish(self, message={}):
        """
        :param message: message to be publish in JSON format
        """

        self._channel.basic_publish(
            exchange=self.server.exchange,
            routing_key=self.server.routing_key,
            body=str(message)
        )

        logging.info("Published Message: {}".format(message))
        self._connection.close()
