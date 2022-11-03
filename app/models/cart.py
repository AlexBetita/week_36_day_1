from .db import db
from .products_in_cart import products_in_cart


class Cart(db.Model):
    '''
        Relationships:

        One to One: Customer
        Many to Many: Products
    '''

    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    checkedout = db.Column(db.Boolean, default=False)
    quantity = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customers.id'), nullable=False)

    customer = db.relationship('Customer', back_populates='cart')
    products = db.relationship(
        'Product', secondary=products_in_cart, back_populates="carts")
