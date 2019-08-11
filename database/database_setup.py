#!/usr/bin/python
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
        }


class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': str(self.name).lstrip(),
            'course': str(self.course).lstrip(),
            'description': str(self.description).lstrip(),
            'price': str(self.price).lstrip(),
            'restaurant_id': self.restaurant_id,
        }


engine = create_engine('sqlite:///database/restaurantmenu.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
