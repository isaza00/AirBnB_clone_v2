#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

import os
from sqlalchemy import (create_engine)
from base_model import Base
from sqlalchemy.orm import sessionmaker


USER = os.getenv('HBNB_MYSQL_USER')
PWD = os.getenv('HBNB_MYSQL_USER')
HOST = os.getenv('HBNB_MYSQL_HOST')
DB = os.getenv('HBNB_MYSQL_DB')
ENV = os.getenv('HBNB_ENV')

Base.metadata.create_all(engine)

class DBStorage:
    """class for db storage"""

    __engine = None
    __session = None

    def __init__(self):
        """ initializes DBStorage instance """
        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(USER,
                                             PWD,
                                             HOST,
                                             DB),
        pool_pre_ping=True)
        if ENV == "test":
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        self.session = 

    query on the current database session (self.__session) all objects depending of the class name (argument cls)
    if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
    this method must return a dictionary: (like FileStorage)
        key = <class-name>.<object-id>
        value = object

