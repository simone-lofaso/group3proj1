from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DateField, BooleanField, SubmitField, FileField, TextAreaField
from wtforms import validators
from wtforms.validators import DataRequired, Length, NumberRange

class SaveBillingInfo(FlaskForm):
    name = StringField('First and last name',
                       validators=[DataRequired()])
    billingAddress = StringField('Address',
                                 validators=[DataRequired()])
    cardNumber = IntegerField('Card Number',
                              validators=[DataRequired()])
    expirationDate = DateField('Expiration Date', format='%m-%Y',
                               validators=[DataRequired()])
    securityNumber = PasswordField('Sec Code',
                                   validators=[DataRequired(), 
                                   Length(min=3, max=3)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Done')

class PostProductForSale(FlaskForm):
    name = StringField('Name of Product', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    item_image = FileField('Image of Product')
    submit = SubmitField('Post')
