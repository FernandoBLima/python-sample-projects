from api.models.base import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseConnection():

    def __init__(self, host="localhost", port=27017, db_name='indexer',
                 username='', password=''):
        self.host = 'postgres_db'
        self.port = '5432'
        self.name = 'pokedex'
        self.username = 'postgres'
        self.password = 'postgres'

    def create_database(self):
        # Connecto to the database
        db_string = 'postgres+psycopg2://{}:{}@{}:{}/{}'.format(
            self.username, self.password, self.host, self.port, self.name)
        engine = create_engine(db_string)
        Base.metadata.create_all(engine, checkfirst=True)

        for _t in Base.metadata.tables:
            print("Table: ", _t)

        # inspector = inspect(engine)
        # print(inspector.get_table_names())

        # Get column information
        # print(inspector.get_columns('trainers'))

        return engine

    def create_session(self, engine):
        # create a configured "Session" class
        Session = sessionmaker(bind=engine)
        # create a Session
        session = Session()

        return session
