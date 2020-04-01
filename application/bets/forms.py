from flask_wtf import FlaskForm
from wtforms import DecimalField, validators

class PlaceBetForm(FlaskForm):
    amount = DecimalField("bet amount")

    class Meta:
        csrf = False
