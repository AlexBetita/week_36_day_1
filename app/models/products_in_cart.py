from .db import db

products_in_cart = db.Table(
    "products_in_cart",
    db.Model.metadata,
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True),
    db.Column("cart_id", db.Integer, db.ForeignKey("carts.id"), primary_key=True))