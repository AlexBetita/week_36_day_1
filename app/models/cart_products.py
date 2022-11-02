from .db import db

cart_products = db.Table(
  "cart_products",
  db.Model.metadata,
  db.Column("cart_id", db.Integer, db.ForeignKey("carts.id"), primary_key=True),
  db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True)
)
