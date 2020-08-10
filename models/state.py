#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref='state',
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """ getter method for cities """
        cities = []
        filestorage = storage._FileStorage__objects
        for key, value in filestorage.items():
            lista = key.split()
            if lista[0] == "City":
                if value.to_dict()[state_id] == self.id:
                    cities.append(value)
        return cities
