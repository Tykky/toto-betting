from flask import render_template, request, redirect, url_for, abort
from application import app, login_required, db
from application.races.models import Race
from application.bets.models import Bet
from application.bets.forms import PlaceBetForm
from flask_login import current_user

@app.route("/bets", methods=['GET'])
@login_required(role="USER")
def bets():
    races = Race.query.all()
    return render_template("/bets/bets.html",races = races, form = PlaceBetForm())

@app.route("/bets/<raceid>", methods=['GET','POST'])
@login_required(role="USER")
def place_bet(raceid):
    race = Race.query.get(raceid)
    if race and request.method == "GET":
        return render_template("/bets/place.html", race=race, form = PlaceBetForm())

    if race and race.isopen:
        form = PlaceBetForm(request.form)
        amount = form.amount.data
        if amount and current_user.credits - amount >= 0:
            bet = Bet(amount, current_user.get_id(), raceid, 2)
            current_user.credits = current_user.credits - amount
            db.session().add(bet)
            db.session().commit()
        else:
            return abort(400)
    else:
        return abort(400)

    return redirect(url_for('bets'))


