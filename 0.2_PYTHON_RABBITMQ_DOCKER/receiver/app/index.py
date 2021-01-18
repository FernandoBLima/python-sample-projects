import pika
import ast
import logging

from enums import EnvironmentVariables


class RabbitMQServerConfigure():

    def __init__(self, host='localhost', queue='hello'):
        """ Server initialization   """

        self.host = host
        self.queue = queue


class rabbitMQServer():
    """Producer component that will publish message and handle
    connection and channel interactions with RabbitMQ.
    """

    def __init__(self, server):
        """
        :param server: Object of class RabbitMQServerConfigure
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
        self._tem = self._channel.queue_declare(
            queue=self.server.queue, durable=False)

    @staticmethod
    def callback(ch, method, properties, body):

        Payload = body.decode("utf-8")
        Payload = ast.literal_eval(Payload)
        logging.info("Data Received : {}".format(Payload))

    def start_server(self):
        self._channel.basic_consume(
            queue=self.server.queue,
            on_message_callback=rabbitMQServer.callback,
            auto_ack=True
        )
        logging.info('Server started waiting for Messages ')
        self._channel.start_consuming()


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    server_configure = RabbitMQServerConfigure(
        host=EnvironmentVariables.RABBITMQ_HOST.get_env(),
        queue=EnvironmentVariables.RABBITMQ_QUEUE.get_env()
    )
    server = rabbitMQServer(server=server_configure)
    server.start_server()
