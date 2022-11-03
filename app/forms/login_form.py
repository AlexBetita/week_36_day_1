from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    customer_name= StringField("Customer name", validators=[DataRequired()])
    phone = IntegerField("Phone number", validators=[DataRequired()])
    submit = SubmitField("Login")
