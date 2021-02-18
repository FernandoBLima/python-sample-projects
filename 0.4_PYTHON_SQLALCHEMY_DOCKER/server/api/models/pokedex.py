from api.models.base import Base

from sqlalchemy import Boolean, Column, Float, Integer, String


class Pokedex(Base):
    __tablename__ = "pokedex"

    number = Column(Integer, primary_key=True)
    legend = Column(Boolean)
    mega = Column(Boolean)
    name = Column(String)
    type_1 = Column(String)
    type_2 = Column(String)
    total = Column(Integer)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    spatk = Column(Integer)
    spdef = Column(Integer)
    speed = Column(Integer)
    height = Column(Float)
    weight = Column(Integer)
    bmi = Column(Float)
    generation = Column(Integer)
