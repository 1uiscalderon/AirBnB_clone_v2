#!/usr/bin/python3
""" State Module for HBNB project for AirBNB_clone_v2"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from os import getenv


class State(BaseModel, Base):
    """ State class definition in the next line"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter attribute cities that returns a list of City instance"""
            from models import storage
            from models.city import City
            new_list = []
            for key, obj_city in storage.all(City).items():
                if obj_city.state_id == self.id:
                    new_list.append(obj_city)
            return new_list
