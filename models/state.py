#!/usr/bin/python3
""""state model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals to the current State.id for FileStorage."""
            from models.city import City
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
