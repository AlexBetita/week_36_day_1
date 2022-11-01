from flask import Blueprint, render_template
from models import Customer

bp = Blueprint("customers", __name__, url_prefix="/customers")

@bp.route('/', methods=['GET'])
def display_all_customers():
  customers = Customer.query.all()
  return render_template('customers.html', customers=customers)
