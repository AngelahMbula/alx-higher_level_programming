#!/usr/bin/python3
"""defines a city model"""

from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represent a city for a Mysql database."""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
