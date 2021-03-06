from flask import render_template, request, redirect, url_for, abort
from application import app, login_required, db
from application.races.models import Race
from application.bets.models import Bet
from application.horses.models import Horse
from application.bets.forms import PlaceBetForm
from flask_login import current_user

@app.route("/bets", methods=['GET'])
@login_required(role="USER")
def bets():
    races = Race.query.all()
    return render_template("/bets/bets.html",races = races, form = PlaceBetForm())

@app.route("/bets/<raceid>", methods=['GET'])
@login_required(role="USER")
def place_bet(raceid):
    race = Race.query.get(raceid)
    if race and request.method == "GET":
        return render_template("/bets/place.html", race=race, form = PlaceBetForm())

    return redirect(url_for('bets'))

@app.route("/bets/<raceid>/confirm/<horseid>", methods=['GET','POST'])
@login_required(role="USER")
def place_bet_confirm(raceid,horseid):
    if request.method == 'GET':

        horse = Horse.query.get(horseid)
        race = Race.query.get(raceid)

        if horse and race:
            return render_template("/bets/place_confirm.html",horse=horse, race=race, form=PlaceBetForm())

        return redirect(url_for('place_bet'))

    # Make transaction

    form = PlaceBetForm(request.form)
    
    if not form.validate():
        return render_template("/bets/bets.html", races=Race.query.all(), form = form)

    amount = round(form.amount.data,2)

    if current_user.credits - amount >= 0:
        current_user.credits = current_user.credits - amount
        bet = Bet(amount,current_user.userid, raceid, horseid)
        db.session().add(bet)
        db.session().commit()
        return redirect(url_for('bets'))

    races = Race.query.all()
    return render_template("/bets/bets.html", races=races, form = PlaceBetForm(), 
    error="Transaction failed. Your account doesn't have sufficient funds.")

