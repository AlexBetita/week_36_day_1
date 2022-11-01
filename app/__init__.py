import os

from flask import Flask
from .config import Configuration
from .models import db, Customer, Orders
from .routes import bp


app = Flask(__name__)
app.config.from_object(Configuration)
DB_FILE = os.environ.get("DATABASE_URL")
db.init_app(app)

app.register_blueprint(routes.bp)


with app.app_context():
	db.drop_all()
	db.create_all()
	customer1 = Customer(customer_name='Alex', last_name = 'Betita', first_name = 'Alex', phone = 800-628-8737)
	customer2 = Customer(customer_name='Danny', last_name = 'Wong', first_name = 'Danny', phone = 877-478-7452)
	customer3 = Customer(customer_name='Stanley', last_name = 'Ou', first_name = 'Stan', phone = 911)
	customer4 = Customer(customer_name='Larry', last_name = 'Liao', first_name = 'Lar', phone = 678-999-8212)

	order1 = Orders(order_date = "12/22/2009 14:00:10", shipped_date = "12/22/2009 12:00:10", status = True, comments = 'Hurry', customer_id = 1)
	order2 = Orders(order_date = "12/22/2009 14:00:10", shipped_date = "12/22/2009 13:00:10", status = True, comments = 'Cmon', customer_id = 2)
	order3 = Orders(order_date = "12/22/2009 14:00:10", shipped_date = "12/22/2009 14:00:10", status = True, comments = 'Maaaan', customer_id = 3)
	order4 = Orders(order_date = "12/22/2009 14:00:10", shipped_date = "12/22/2009 15:00:10", status = True, comments = 'Plox', customer_id = 4)

	db.session.add(customer1)
	db.session.add(customer2)
	db.session.add(customer3)
	db.session.add(customer4)

	db.session.add(order1)
	db.session.add(order2)
	db.session.add(order3)
	db.session.add(order4)

	db.session.commit()
