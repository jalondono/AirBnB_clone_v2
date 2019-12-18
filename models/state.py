#!/usr/bin/python3
"""This is the state class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="states", cascade="delete")
