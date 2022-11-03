import os

from datetime import datetime

from flask import Flask
from .config import Configuration

from .models import db, Customer, Order, Product, order_details
from .routes import customers_bp, products_bp, main_bp


app = Flask(__name__)
app.config.from_object(Configuration)
DB_FILE = os.environ.get("DATABASE_URL")
db.init_app(app)

app.register_blueprint(customers_bp)
app.register_blueprint(products_bp)
app.register_blueprint(main_bp)


# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     customer1 = Customer(customer_name='Alex', last_name='Betita',
#                          first_name='Alex', phone=800-628-8737)
#     customer2 = Customer(customer_name='Danny', last_name='Wong',
#                          first_name='Danny', phone=877-478-7452)
#     customer3 = Customer(customer_name='Stanley',
#                          last_name='Ou', first_name='Stan', phone=911)
#     customer4 = Customer(customer_name='Larry', last_name='Liao',
#                          first_name='Lar', phone=678-999-8212)

#     order1 = Order(order_date=datetime.now(), shipped_date=datetime.now(
#     ), status=True, comments='Hurry', customer_id=1)
#     order2 = Order(order_date=datetime.now(), shipped_date=datetime.now(
#     ), status=True, comments='Cmon', customer_id=2)
#     order3 = Order(order_date=datetime.now(), shipped_date=datetime.now(
#     ), status=True, comments='Maaaan', customer_id=3)
#     order4 = Order(order_date=datetime.now(), shipped_date=datetime.now(
#     ), status=True, comments='Plox', customer_id=4)

#     product1 = Product(product_name='Toy', vendor='ToysRUs',
#                        product_type='unsafe toy', quantity_in_stock=100000, price=10000000)

#     db.session.add(customer1)
#     db.session.add(customer2)
#     db.session.add(customer3)
#     db.session.add(customer4)

#     db.session.add(order1)
#     db.session.add(order2)
#     db.session.add(order3)
#     db.session.add(order4)

#     db.session.add(product1)

#     db.session.commit()
