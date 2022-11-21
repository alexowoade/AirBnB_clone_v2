#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from models.place import place_amenity
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    ''' defines Amenity class '''
    if storage_type == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)
    else:
        name = ''
