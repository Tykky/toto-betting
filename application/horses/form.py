from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
from wtforms.widgets import TextArea

class AddHorseForm(FlaskForm):

    name = StringField("Horse name",[validators.length(min=2,max=12)])
    breed = StringField("Horse breed",[validators.length(min=2,max=16)])
    tier = SelectField("Tier", choices=[(1,1),(2,2),(3,3),(4,4),(5,5)], validators=[validators.input_required()])
    description = StringField("Description", widget=TextArea())
  
    class Meta:
        csrf = False