from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectMultipleField, SelectField
from wtforms.widgets import TextArea

class AddRaceForm(FlaskForm):
    name = StringField("Race name",[validators.length(min=2,max=16)])
    location = StringField("Location",[validators.length(min=2,max=16)])
    description = StringField("Description", widget=TextArea(), validators=[validators.length(max=2000)])

    class Meta:
        csrf = False
