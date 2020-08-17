#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

import os
from sqlalchemy import (create_engine)
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


USER = os.getenv('HBNB_MYSQL_USER')
PWD = os.getenv('HBNB_MYSQL_PWD')
HOST = os.getenv('HBNB_MYSQL_HOST')
DB = os.getenv('HBNB_MYSQL_DB')
ENV = os.getenv('HBNB_ENV')


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
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ show all objects cls as dictionary """
        dic = {}
        models = {'State': State,
                  'City': City,
                  'User': User,
                  'Place': Place,
                  'Review': Review,
                  'Amenity': Amenity
                  }
        if cls is None:
            for cls in models:
                model = models[cls]
                query = DBStorage.__session.query(model)
                for row in query:
                    delattr(row, '_sa_instance_state')
                    key = row.__class__.__name__ + '.' + row.id
                    dic[key] = row

        else:
            model = models[cls]
            query = DBStorage.__session.query(model)
            for row in query:
                delattr(row, '_sa_instance_state')
                key = row.__class__.__name__ + '.' + row.id
                dic[key] = row
        return dic

    def new(self, obj):
        """ add the object to the current database session """
        DBStorage.__session.add(obj)

    def save(self):
        """ commit all changes of the current db session """
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """ delete from the current db session obj if not None """
        DBStorage.__session.delete(obj)

    def reload(self):
        """ create all tables in db """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()
