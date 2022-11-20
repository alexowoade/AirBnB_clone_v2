#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    ''' defines State class '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # db storage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    # file storage
    @property
    def cities(self):
        all_cities = models.storage.all(City)
        return [city for city in all_cities.values()
                if city.state_id == self.id]
