import os
from enum import Enum


class EnvironmentVariables(str, Enum):
    SERVICE = 'SERVICE'
    RABBITMQ_USER_DEFAULT = 'RABBITMQ_USER_DEFAULT'
    RABBITMQ_PASS_DEFAULT = 'RABBITMQ_PASS_DEFAULT'
    RABBITMQ_HOST = 'RABBITMQ_HOST'
    RABBITMQ_QUEUE = 'RABBITMQ_QUEUE'
    RABBITMQ_ROUTING_KEY = 'RABBITMQ_ROUTING_KEY'
    SERVER_PORT = 'SERVER_PORT'
    SERVER_HOST = 'SERVER_HOST'

    def get_env(self, variable=None):
        return os.environ.get(self, variable)
