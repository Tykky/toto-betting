from flask_wtf import FlaskForm
from wtforms import DecimalField

class PlaceBetForm(FlaskForm):
    amount = DecimalField("bet amount")

    class Meta:
        csrf = False
