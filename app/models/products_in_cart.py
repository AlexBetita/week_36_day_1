from .db import db

# products_in_cart = db.Table(
#     "products_in_cart",
#     db.Model.metadata,
#     db.Column("product_id", db.Integer, db.ForeignKey(
#         "products.id"), primary_key=True),
#     db.Column("cart_id", db.Integer, db.ForeignKey("carts.id"), primary_key=True))


class ProductsInCart(db.Model):
    '''
        Relationships:

        Many to One: Cart
        Many to One: Product
    '''

    __tablename__ = "products_in_carts"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    carts_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    products_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)

    cart = db.relationship('Cart', back_populates='products')
    products = db.relationships('Product', back_populates='carts')
