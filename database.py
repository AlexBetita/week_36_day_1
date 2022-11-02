from app import app, db 
from dotenv import load_dotenv
load_dotenv()
from app.models import Customer, Orders, Product, order_details
from datetime import datetime

with app.app_context():
	db.drop_all()
	db.create_all()
	customer1 = Customer(customer_name='Alex', last_name = 'Betita', first_name = 'Alex', phone = 800-628-8737)
	customer2 = Customer(customer_name='Danny', last_name = 'Wong', first_name = 'Danny', phone = 877-478-7452)
	customer3 = Customer(customer_name='Stanley', last_name = 'Ou', first_name = 'Stan', phone = 911)
	customer4 = Customer(customer_name='Larry', last_name = 'Liao', first_name = 'Lar', phone = 678-999-8212)

	order1 = Orders(order_date = datetime.now(), shipped_date = datetime.now(), status = True, comments = 'Hurry', customer_id = 1)
	order2 = Orders(order_date = datetime.now(), shipped_date = datetime.now(), status = True, comments = 'Cmon', customer_id = 2)
	order3 = Orders(order_date = datetime.now(), shipped_date = datetime.now(), status = True, comments = 'Maaaan', customer_id = 3)
	order4 = Orders(order_date = datetime.now(), shipped_date = datetime.now(), status = True, comments = 'Plox', customer_id = 4)

	product1 = Product(product_name = 'Toy', vendor = 'ToysRUs', product_type = 'unsafe toy', quantity_in_stock = 100000, price = 10000000)
	product2 = Product(product_name = 'Gun', vendor = 'GunsRUs', product_type = 'unsafe toy', quantity_in_stock = 100000, price = 10000000)
	product3 = Product(product_name = 'Energy Drink', vendor = 'EnRGrUs', product_type = 'unsafe toy', quantity_in_stock = 100000, price = 10000000)
	product4 = Product(product_name = 'Wig', vendor = 'WigRUs', product_type = 'unsafe toy', quantity_in_stock = 100000, price = 10000000)

	db.session.add(customer1)
	db.session.add(customer2)
	db.session.add(customer3)
	db.session.add(customer4)

	db.session.add(order1)
	db.session.add(order2)
	db.session.add(order3)
	db.session.add(order4)

	db.session.add(product1)
	db.session.add(product2)
	db.session.add(product3)
	db.session.add(product4)
  
product1.orders.append(order1)
product1.orders.append(order2)
product2.orders.append(order1)
product3.orders.append(order3)
product2.orders.append(order3)
product2.orders.append(order2)
product3.orders.append(order1)
product4.orders.append(order4)
order4.products.append(product4)

db.session.commit()