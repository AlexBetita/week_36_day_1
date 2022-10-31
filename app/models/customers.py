# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.schema import Column
# from sqlalchemy.types import Integer, String

from .db import db


# Base = declarative_base()

# class Customer(Base):

# 	__tablename__ = 'customers'

# 	id = Column(Integer, primary_key=True)
# 	customer_name = Column(String)
# 	last_name = Column(String)
# 	first_name = Column(String)
# 	phone = Column(Integer)

class Customer(db.Model):

	__tablename__ = 'customers'

	id = db.Column(db.Integer, primary_key=True)
	customer_name = db.Column(db.String)
	last_name = db.db.Column(db.String)
	first_name = db.Column(db.String)
	phone = db.Column(db.Integer)
