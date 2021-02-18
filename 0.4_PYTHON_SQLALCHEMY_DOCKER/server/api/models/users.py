from api.models.base import Base

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String,)
    last_name = Column(String)
    age = Column(Integer)
