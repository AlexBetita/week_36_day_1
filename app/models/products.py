from .db import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    vendor = db.Column(db.String)
    product_type = db.Column(db.String)
    quantity_in_stock = db.Column(db.Integer)
    price = db.Column(db.Integer)