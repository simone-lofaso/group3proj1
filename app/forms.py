from wtforms import form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import SubmitField

class SearchForm(form.Form):
    search = StringField('search', [DataRequired()])
    submit = SubmitField("Submit")
