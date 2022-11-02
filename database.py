from app import app, db 
from dotenv import load_dotenv
load_dotenv()
from app.models import Customer, Orders, Product, products_in_cart, order_details, Cart
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

	product1 = Product(product_name = 'Toy', vendor = 'ToysRUs', product_type = 'unsafe toy', quantity_in_stock = 100000, price = 10000000, product_img = None)
	product2 = Product(product_name = 'Gun', vendor = 'GunsRUs', product_type = 'unsafe toy', quantity_in_stock = 100000, price = 10000000, product_img = None)
	product3 = Product(product_name = 'Energy Drink', vendor = 'EnRGrUs', product_type = 'unsafe toy', quantity_in_stock = 100000, price = 10000000, product_img = None)
	product4 = Product(product_name = 'Wig', vendor = 'WigRUs', product_type = 'unsafe toy', quantity_in_stock = 100000, price = 10000000, product_img = None)

cart1 = Cart(checkedout = 'False', quantity = 3, customer_id = 1, product_id = 1)
cart2 = Cart(checkedout = 'False', quantity = 2, customer_id = 2, product_id = 2)
cart3 = Cart(checkedout = 'False', quantity = 6, customer_id = 3, product_id = 3)
cart4 = Cart(checkedout = 'False', quantity = 1, customer_id = 4, product_id = 4)

#customers
db.session.add(customer1)
db.session.add(customer2)
db.session.add(customer3)
db.session.add(customer4)

#orders
db.session.add(order1)
db.session.add(order2)
db.session.add(order3)
db.session.add(order4)

#products
db.session.add(product1)
db.session.add(product2)
db.session.add(product3)
db.session.add(product4)

#carts
db.session.add(cart1)
db.session.add(cart2)
db.session.add(cart3)
db.session.add(cart4)
  
# product1.orders.append(order1)
# product2.orders.append(order1)
# product3.orders.append(order1)

# product1.orders.append(order2)
# product2.orders.append(order2)

# product3.orders.append(order3)
# product2.orders.append(order3)
# product1.orders.append(order3)
# product2.orders.append(order3)
# product1.orders.append(order3)
# product4.orders.append(order3)

# product4.orders.append(order4)

#order-details
order4.products.append(product4)

order3.products.append(product4)
order3.products.append(product1)
order3.products.append(product2)
order3.products.append(product1)
order3.products.append(product2)
order3.products.append(product3)

order2.products.append(product2)
order2.products.append(product1)

order1.products.append(product3)
order1.products.append(product2)
order1.products.append(product1)


#favorites
customer1.products.append(product1)
customer2.products.append(product2)

#


customer1.carts

db.session.commit()