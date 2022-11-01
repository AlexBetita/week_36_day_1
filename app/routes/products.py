from flask import Blueprint

bp = Blueprint("products", __name__, url_prefix="/products")

@bp.route('/', methods=['GET'])
def get_all_products():
    pass