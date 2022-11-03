from flask import Blueprint, render_template
from ..models import Order

order_bp = Blueprint("orders", __name__, url_prefix= "/orders")

@order_bp.route('/', methods=['GET'])
def get_all_orders():
    orders = Order.query.all()
    return render_template('orders.')  

@order_bp.route('/<int:id>', methods=['GET'])
def get_order_by_id(id):
    orders = Order.query.get_or_404(id)
    return render_template('order_details.html', orders=orders)