from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField
from wtforms.widgets import TextArea

class AddHorseForm(FlaskForm):

    name = StringField("Horse name")
    breed = StringField("Horse breed")
    tier = IntegerField("Tier")
    description = StringField("Description", widget=TextArea())
  
    class Meta:
        csrf = False
