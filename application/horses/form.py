from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
from wtforms.widgets import TextArea

class AddHorseForm(FlaskForm):

    name = StringField("Horse name")
    breed = StringField("Horse breed")
    tier = SelectField("Tier", choices=[(1,1),(2,2),(3,3),(4,4),(5,5)], validators=[validators.input_required])
    description = StringField("Description", widget=TextArea())
  
    class Meta:
        csrf = False