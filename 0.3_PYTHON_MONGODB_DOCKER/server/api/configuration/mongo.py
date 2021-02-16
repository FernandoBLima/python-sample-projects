# from pymongo import MongoClient
from mongoengine import connect


class MongoConnection():

    def __init__(self, host="localhost", port=27017, db_name='',
                 username='', password=''):
        self.host = host
        self.port = port
        self.db_name = db_name

    def create_database(self):
        client = connect(db=self.db_name, host=self.host, port=int(self.port))
        client['pokemon']
