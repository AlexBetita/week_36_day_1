from .db import db

order_details = db.Table(
    "order_details",
    db.Model.metadata,
    db.Column("customer_id", db.Integer, db.ForeignKey("customers.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True))
