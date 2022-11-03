from flask import Blueprint, render_template
from ..forms import ProductCreateForm
from ..models import Product, db

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.route('/', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@products_bp.route('/<int:id>', methods=['GET'])
def get_product():
    products = Product.query.get(id)
    return render_template('products.html', products=products)

@products_bp.route('/', methods=["POST"])
def create():
    product_form = ProductCreateForm()
    product = Product.query.filter(Product.product_name == product_form.product_name.data).all()

    if not product:
        new_product = Product(
            product_name=product_form.product_name.data,
            vendor=product_form.vendor.data,
            product_type=product_form.product_type.data,
            quantity_in_stock=product_form.quantity_in_stock.data,
            price=product_form.price.data,
            product_img=product_form.product_img.data,
        )
        db.session.add(new_product)
        db.session.commit()
        return render_template('products.html', product=new_product, form=product_form)
    return render_template('products.html', form=product_form)