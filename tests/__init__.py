from unittest import TestCase

import sure  # noqa
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from factory import Faker
from factory.alchemy import SQLAlchemyModelFactory

from sqlalchemy_pagination import paginate


Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class UserFactory(SQLAlchemyModelFactory):
    name = Faker('name')

    class Meta:
        model = User
        sqlalchemy_session = session


class PaginateTest(TestCase):
    def setUp(self):
        Base.metadata.create_all(engine)
        self.total_users = 25
        for i in range(self.total_users):
            UserFactory.create(id=i)
        self.query = session.query(User)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_paginate_total(self):
        pagination = paginate(self.query, 1, 5)
        pagination.total.should.equals(self.total_users)

    def test_paginate_has_previous(self):
        pagination = paginate(self.query, 1, 5)
        pagination.has_previous.should.be(False)
        pagination.previous_page.should.be(None)

    def test_paginate_has_next(self):
        pagination = paginate(self.query, 5, 5)
        pagination.has_next.should.be(False)
        pagination.next_page.should.be(None)

    def test_previous_page(self):
        pagination = paginate(self.query, 2, 5)
        pagination.previous_page.should.equals(1)
        pagination.has_previous.should.be(True)

    def test_next_page(self):
        pagination = paginate(self.query, 1, 5)
        pagination.next_page.should.equals(2)
        pagination.has_next.should.be(True)

    def test_pages(self):
        pagination = paginate(self.query, 1, 3)
        pagination.pages.should.equals(9)

    def test_items(self):
        pagination = paginate(self.query, 1, 5)
        pagination.items.should.have.length_of(5)
        pagination = paginate(self.query, 9, 3)
        pagination.items.should.have.length_of(1)

    def test_out_of_bounds(self):
        pagination = paginate(self.query, 2, 25)
        pagination.items.should.have.length_of(0)
        paginate.when.called_with(self.query, 0, 25).should.throw(AttributeError)
        paginate.when.called_with(self.query, 1, 0).should.throw(AttributeError)
