from flask import render_template, request, redirect, url_for
from application import app, login_required, db
from application.races.forms import AddRaceForm
from application.races.models import Race
from application.horses.models import Horse
from application.auth.models import User
from application.bets.models import Bet
from application.races.models import Connector
import random

@app.route("/races/add", methods=['GET','POST'])
@login_required(role="ADMIN")
def add_race():
    if request.method == "GET":
        races = Race.query.all()
        return render_template("/races/add.html",races = races, form = AddRaceForm())

    form = AddRaceForm(request.form)
    race = Race(form.name.data, form.location.data, form.description.data)

    db.session().add(race)
    db.session().commit()

    return redirect(url_for("add_race"))

@app.route("/races/<raceid>/status", methods=['POST'])
@login_required(role="ADMIN")
def change_race_status(raceid):

    race = Race.query.get(raceid)
    if race:
        if race.isopen:

            # Clear all bets

            horses = race.horses
            bets = Bet.query.filter_by(raceid=raceid)

            rindex = int(random.uniform(1,len(horses))-1)
            print(rindex)
            
            winner = horses[rindex]
            wins = Bet.query.filter_by(horseid=winner.horseid)

            for win in wins:
                user = User.query.get(win.userid)
                user.credits = user.credits + win.amount*2
                db.session().commit()

            winner.wins = winner.wins + 1
            bets.delete()
            race.isopen = False
            db.session().commit()

        elif len(race.horses) >= 2:
            race.isopen = True
            db.session().commit()
        else:
            races = Race.query.all()
            return render_template("/races/add.html", races=races, form=AddRaceForm(),
            error="Cannot open "+race.name+". Race has less than 2 horses!")

    return redirect(url_for("add_race"))

@app.route("/races/<raceid>/delete", methods=['POST'])
@login_required(role="ADMIN")
def delete_race(raceid):

    race = Race.query.filter_by(raceid=raceid)
    if not race.first().isopen:
        if len(race.first().horses) == 0:
            race.delete()
            db.session().commit()
        else:
            races = Race.query.all()
            return render_template("/races/add.html", races=races, form=AddRaceForm(),
            error="Cannot delete "+race.first().name+". There are horses in the race! Remove all "+
            "the horses first.")

    return redirect(url_for('add_race'))

@app.route("/races/<raceid>/edit", methods=['POST','GET'])
@login_required(role="ADMIN")
def edit_race(raceid):
    race = Race.query.filter_by(raceid=raceid).first()
    
    if race and not race.isopen:

        if request.method == 'GET':
            horses = Horse.query.all()
            return render_template("races/edit.html", horses=horses, race=race, form=AddRaceForm(name=race.name,
            location=race.location, description=race.description))

        form = AddRaceForm(request.form)
        race.name = form.name.data
        race.location = form.location.data
        race.description = form.description.data
        db.session().commit()

    return redirect(url_for('add_race'))

@app.route("/races/<raceid>/edit/addhorse/<horseid>", methods=['POST'])
@login_required(role="ADMIN")
def add_horse_to_race(raceid, horseid):

    horse = Horse.query.filter_by(horseid=horseid).first()

    if horse and not horse.contains_raceid(raceid):
        connector = Connector(raceid,horseid)
        db.session().add(connector)
        db.session().commit()

    return redirect(url_for('edit_race', raceid=raceid))

@app.route("/races/<raceid>/edit/removehorse/<horseid>", methods=['POST'])
@login_required(role="ADMIN")
def remove_horse_from_race(raceid, horseid):

    horse = Horse.query.filter_by(horseid=horseid).first()
    race = Race.query.filter_by(raceid=raceid).first()

    if horse and race:
        connector = Connector.query.filter_by(raceid=raceid, horseid=horseid)
        if connector.first():
            connector.delete()
            db.session().commit()

    return redirect(url_for('edit_race', raceid=raceid))
