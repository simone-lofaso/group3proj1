from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DateField, BooleanField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Length, NumberRange

class SaveBillingInfo(FlaskForm):
    name = StringField('First and last name',
                       validators=[DataRequired()])
    billingAddress = StringField('Address',
                                 validators=[DataRequired()])
    cardNumber = IntegerField('Card Number',
                             validators=[DataRequired(),
                             NumberRange(min=16, max=16)])
    expirationDate = DateField(format='%m/%Y',
                               validators=[DataRequired()])
    securityNumber = PasswordField('Sec Code',
                                   validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Done')
