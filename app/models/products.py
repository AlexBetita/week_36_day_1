from .db import db
from .order_details import order_details
from .favorites import favorites
from .products_in_cart import products_in_cart


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    vendor = db.Column(db.String)
    product_type = db.Column(db.String)
    quantity_in_stock = db.Column(db.Integer)
    price = db.Column(db.Integer)
    product_img = db.Column(db.Text(400))


    orders = db.relationship("Order", secondary=order_details, back_populates="products")
    customers = db.relationship("Customer", secondary=favorites, back_populates="products")
    carts = db.relationship("Cart", secondary=products_in_cart, back_populates="products" )
    comments = db.relationship("Comment", back_populates="product" )
