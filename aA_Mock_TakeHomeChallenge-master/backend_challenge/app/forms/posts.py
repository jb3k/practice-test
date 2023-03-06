from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError


class PostForm(FlaskForm):
  
    title = StringField('Title', validators=[DataRequired()])
    rating = IntegerField(5, validators=[DataRequired()])
    coffee = StringField('Coffee', validators=[DataRequired()])
    post = StringField('Post', validators=[DataRequired()])
