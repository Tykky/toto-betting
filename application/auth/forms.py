from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Username")
    password1 = PasswordField("Password")
    password2 = PasswordField("Retype password")

    class Meta:
        csrf = False


