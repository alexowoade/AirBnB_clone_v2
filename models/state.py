#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    ''' defines State class '''
    # name = ''

    # db storage
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    # file storage
    @property
    def cities(self):
        all_cities = models.storage.all(City)
        return [city for city in all_cities.values()
                if city.state_id == self.id]
