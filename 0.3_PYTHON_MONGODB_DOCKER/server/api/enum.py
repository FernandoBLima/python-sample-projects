import os
from enum import Enum


class EnvironmentVariables(str, Enum):
    NAME_DATABASE = 'NAME_DATABASE'
    USER_DATABASE = 'USER_DATABASE'
    PASSWORD_DATABASE = 'PASSWORD_DATABASE'
    HOST_DATABASE = 'HOST_DATABASE'
    PORT_DATABASE = 'PORT_DATABASE'

    def get_env(self, variable=None):
        return os.environ.get(self, variable)
