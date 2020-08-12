#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(integer, nullable=False, default=0)
    number_bathrooms = Column(integer, nullable=False, default=0)
    max_guest = Column(integer, nullable=False, default=0)
    price_by_night = Column(integer, nullable=False, default=0)
    latitude = Column(float)
    longitude = Column(float)
    amenity_ids = []
