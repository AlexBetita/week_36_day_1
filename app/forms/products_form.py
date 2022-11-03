from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SubmitField, IntegerField
)
from wtforms.validators import DataRequired

class ProductCreateForm(FlaskForm):
    product_name = StringField("Product Name", [DataRequired()])
    vendor = StringField("Vendor", [DataRequired()])
    product_type = StringField("Product Type", [DataRequired()])
    quantity_in_stock = IntegerField("Vendor", [DataRequired()])
    vendor = StringField("Vendor", [DataRequired()])
    product_img = StringField("Product Image URL", [DataRequired()])
    submit = SubmitField("Submit")
