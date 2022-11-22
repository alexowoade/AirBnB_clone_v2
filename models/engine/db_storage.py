#!/usr/bin/python3
''' creates a new engine, db_storage '''
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session


class DBStorage:
    ''' sets up the db storage engine '''
    __engine = None
    __session = None
    classes = [State, City, User, Amenity, Place, Review]

    def __init__(self):
        user, pwd = getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD')
        host, db = getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        url = f'mysql+mysqldb://{user}:{pwd}@{host}/{db}'

        self.__engine = create_engine(url, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ''' returns dictionary of objects '''
        obj_dict = {}
        if cls is None:
            for c in DBStorage.classes:
                try:
                    obj_list = self.__session.query(c).all()
                except Exception:
                    continue
                for obj in obj_list:
                    key = type(obj).__name__ + '.' + obj.id
                    obj_dict[key] = obj
            return obj_dict

        if type(cls) is str:
            cls = eval(cls)
        obj_list = self.__session.query(cls).all()
        for obj in obj_list:
            key = type(obj).__name__ + '.' + obj.id
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        ''' adds a new record (object) to table '''
        self.__session.add(obj)

    def save(self):
        ''' saves a new record (object) to table '''
        self.__session.commit()

    def delete(self, obj=None):
        ''' deletes object (record) from table '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        ''' reload engine '''
        print(self)
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        ''' close session '''
        self.__session.close()
