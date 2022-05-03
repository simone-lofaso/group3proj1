from flask_wtf import FlaskForm
from wtforms import FileField, StringField, DecimalField, SubmitField, HiddenField
from wtforms.validators import DataRequired
class ItemForm(FlaskForm):
    item_name = StringField("Item Name", [DataRequired()])
    item_description = StringField('Item Description', [DataRequired()])
    item_price = DecimalField('Item Price', [DataRequired()])
    submit = SubmitField('create item')
    
class SearchForm(FlaskForm):
    search_term = StringField("Search", [DataRequired()])
    
class AddToCartForm(FlaskForm):
    id = HiddenField(validators=[DataRequired()])
    submit = SubmitField(label="Add To Cart")
    
class LoginForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = StringField("Password", [DataRequired()])
    item_id = HiddenField(validators=[DataRequired()])
    submit = SubmitField(label = "Login")
