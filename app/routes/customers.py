from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from ..models import Customer
from ..forms import LoginForm

customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route('/<int:id>', methods=['GET'])
def customers(id):
  customers = [Customer.query.get_or_404(id)] if id else Customer.query.all()
  return render_template('customers.html', customers=customers)

@customers_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for(".customers"))

    form = LoginForm()
    if form.validate_on_submit():
        customer = Customer.query.filter(Customer.customer_name == form.customer_name.data).first()

        if not customer or not customer.check_phone(form.phone.data):
            return redirect(url_for(".login"))

        login_user(customer)
        return redirect(url_for(".customers"))

    return render_template("login.html", form=form)

@customers_bp.route('/logout', methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for('.login'))
