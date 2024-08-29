from app.data_base import Base
from sqlalchemy import  Column, String, Integer, Double

class Beers(Base):
    __tablename__ = 'Beers'

    name = Column(String, primary_key=True)
    sort = Column(Integer)
    description = Column(String)
    fortress = Column(Double)
    iconurl = Column(String)

class Sort(Base):
    __tablename__ = 'Sort'

    id_sort = Column(Integer, primary_key=True)
    sort = Column(String)

class FeedBack(Base):
    __tablename__ = 'FeedBack'

    id_feedback = Column(Integer, primary_key=True)
    name = Column(String)
    comment = Column(String, nullable=False)
    nick = Column(String, nullable=False)
    estimation = Column(Integer, nullable=False)