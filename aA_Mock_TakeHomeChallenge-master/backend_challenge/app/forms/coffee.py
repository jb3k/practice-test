from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired, ValidationError


class CoffeeForm(FlaskForm):
  
    name = StringField('Name', validators=[DataRequired()])
    year = IntegerField(4, validators=[DataRequired()])
    caffine = DecimalField(2, places=2, validators=[DataRequired()])
