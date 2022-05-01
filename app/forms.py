from flask_wtf import FlaskForm
from wtforms import FileField, StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired
class ItemForm(FlaskForm):
    item_name = StringField("Item Name", [DataRequired()])
    item_description = StringField('Item Description', [DataRequired()])
    item_price = DecimalField('Item Price', [DataRequired()])
    item_picture = FileField('Item Picture')
    submit = SubmitField('create item')
    
class SearchForm(FlaskForm):
    search_term = StringField("Search", [DataRequired()])
    
