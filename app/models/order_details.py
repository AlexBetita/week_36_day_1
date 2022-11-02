from .db import db

order_details = db.Table(
    "order_details",
    db.Model.metadata,
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True))
