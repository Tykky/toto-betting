from flask_wtf import FlaskForm
from wtforms import StringField

class AddRaceForm(FlaskForm):
    name = StringField("Race name")
    location = StringField("Location")
    description = StringField("Description")

    class Meta:
        csrf = False
