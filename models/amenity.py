#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Amenity(BaseModel):
    """Amenities of places"""
    __tablename__ = "amenities"
    name = column(string(128), nullable=False)

