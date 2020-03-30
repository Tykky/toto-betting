from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    pminlength = 8
    username = StringField("Username", [validators.length(min=2,max=12)])
    password1 = PasswordField("Password", [validators.length(min=pminlength)])
    password2 = PasswordField("Retype password", [validators.length(min=pminlength)])

    class Meta:
        csrf = False


