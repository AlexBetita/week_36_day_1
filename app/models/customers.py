from .db import db
from .favorites import favorites


class Customer(db.Model):
    """
                Relationships:

                One to One: Cart
                One to Many: Orders
                One to Many: Favorites
    """
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String)
    last_name = db.db.Column(db.String)
    first_name = db.Column(db.String)
    phone = db.Column(db.Integer)
    balance = db.Column(db.Integer)
    profile_img = db.Column(db.Text(400))

    cart = db.relationship('Cart', back_populates='customer')
    products = db.relationship('Product', secondary=favorites, back_populates="customers")
    orders = db.relationship("Order", back_populates="customer")
