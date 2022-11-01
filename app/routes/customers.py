from flask import Blueprint

bp = Blueprint("customers", __name__, url_prefix="/customers")

@bp.route('/', methods=['GET'])
def get_all_customers():
  pass
