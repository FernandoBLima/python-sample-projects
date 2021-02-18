from api.models.base import Base

from sqlalchemy import Column, Integer, String


class Trainers(Base):
    __tablename__ = "trainers"

    name = Column(String, primary_key=True)
    region = Column(String)
    age = Column(Integer)
