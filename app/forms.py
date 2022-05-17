from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DateField, BooleanField, SubmitField, FileField, TextAreaField, DecimalField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange
    
#Creates forms for users to enter information    
class SearchForm(FlaskForm):
    search_term = StringField("Search", validators=[DataRequired()])
    submit = SubmitField(label="Search")

class AddToCartForm(FlaskForm):
    id = HiddenField(validators=[DataRequired()])
    remove = HiddenField(validators=[DataRequired()])
    submit = SubmitField(label="Add To Cart")
    
class LoginForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = StringField("Password", [DataRequired()])
    remove = HiddenField(validators=[DataRequired()])
    item_id = HiddenField(validators=[DataRequired()])
    submit = SubmitField(label = "Login")
    
class RemoveFromCart(FlaskForm):
    item_id = HiddenField(validators=[DataRequired()])
    remove = HiddenField(validators=[DataRequired()])
    submit = SubmitField(label="Remove From Cart")
    
class ItemDescriptionForm(FlaskForm):
    item_id = HiddenField(validators=[DataRequired()])
    go_to = SubmitField(label='Visit Item')
    
class SaveBillingInfo(FlaskForm):
    name = StringField('First and last name',
                       validators=[DataRequired()])
    billingAddress = StringField('Address',
                                 validators=[DataRequired()])
    cardNumber = IntegerField('Card Number',
                              validators=[DataRequired()])
    expirationDate = DateField('Expiration Date',
                               validators=[DataRequired()])
    secCode = PasswordField('Sec Code',
                                   validators=[DataRequired(), 
                                   Length(min=3, max=3)])
    submit = SubmitField('Done')

class PostProductForSale(FlaskForm):
    name = StringField('Name of Product', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    item_image = StringField('Image of Product')
    submit = SubmitField('Post')
