from flask import render_template
from application import app, login_required
from application.races.models import Race
from application.bets.forms import PlaceBetForm

@app.route("/bets", methods=['GET'])
@login_required(role="USER")
def bets():
    races = Race.query.all()
    return render_template("/bets/bets.html",races = races, form = PlaceBetForm())



