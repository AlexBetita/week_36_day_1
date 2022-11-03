from flask import Blueprint, render_template
from ..models import Product

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.route('/', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@products_bp.route('/<int:id>', method=['GET'])
def get_product():
    products = Product.query.get(id)
    return render_template('products.html', products=products)

# @products_bp.route('/', method=["POST"])
# def create_a_product():
#     pass