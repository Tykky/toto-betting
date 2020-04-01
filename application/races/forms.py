from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.widgets import TextArea

class AddRaceForm(FlaskForm):
    name = StringField("Race name")
    location = StringField("Location")
    description = StringField('Description', widget=TextArea(), validators=[validators.length(max=2000)])

    class Meta:
        csrf = False
