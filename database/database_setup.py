#!/usr/bin/python
import datetime
from sqlalchemy import \
    create_engine, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'create_date': self.create_date.isoformat(),
        }


class Item(Base):
    __tablename__ = 'item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    owner_id = Column(String(80))
    category_id = Column(Integer, ForeignKey('category.id'))
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
    category = relationship(Category)
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': str(self.name).lstrip(),
            'description': str(self.description).lstrip(),
            'owner_id': str(self.owner_id).lstrip(),
            'category_id': self.category_id,
            'create_date': self.create_date.isoformat(),
        }

# 'check_same_thread' fix for sqlalchemy bug caused by refreshing or switching
# pages too quickly - Citation:
# https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa
engine = create_engine('sqlite:///database/catalog.db',
                       connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
