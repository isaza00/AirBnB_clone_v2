#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float
from sqlalchemy import String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review",
                           backref='place',
                           cascade="all, delete-orphan")

    place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id',
               String(60),
               ForeignKey('places.id'),
               nullable=False),
        Column('amenity_id',
               String(60),
               ForeignKey('amenities.id'),
               nullable=False))

    amenities = relationship("Amenity",
                             secondary=place_amenity,
                             viewonly=False)

    @property
    def reviews(self):
        """ return reviews for place """
        from models import storage
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            return
        reviews = []
        filestorage = storage._FileStorage__objects
        for key, value in filestorage.items():
            lista = key.split(".")
            if lista[0] == "Review":
                if value.to_dict()["place_id"] == self.id:
                    reviews.append(value)
        return reviews
