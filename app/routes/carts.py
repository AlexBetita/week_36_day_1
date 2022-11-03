from flask import Blueprint, render_template, request
from ..models import Cart

carts_bp = Blueprint("carts", __name__, url_prefix="/carts")


@carts_bp.route('/<int:id>', methods=['GET'])
def cart_detail(id):
    cart = Cart.query.get_or_404(id)
    return cart
