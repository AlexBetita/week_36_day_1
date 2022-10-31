from .db import db

class Orders(db.Model):

	__tablename__ = 'orders'

	id = db.Column(db.Integer, primary_key=True)
	order_date = db.Column(db.DateTime)
	shipped_date = db.Column(db.DateTime)
	status = db.Column(db.Boolean)
	comments = db.Column(db.Text(3000)) #3kb
	customer_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='CASCADE'))