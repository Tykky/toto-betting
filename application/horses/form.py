from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validator
  
class LoginForm(FlaskForm):

    name = StringField("Horse name")
    breed = StringField("Horse breed")
    tier = Inte
  
    class Meta:
        csrf = False
