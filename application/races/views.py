from flask import render_template, request, redirect, url_for
from application import app, login_required, db
from application.races.forms import AddRaceForm
from application.races.models import Race
from application.horses.models import Horse
from application.races.models import Connector

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
    if race.isopen:
        race.isopen = False
    else:
        race.isopen = True

    db.session().commit()

    return redirect(url_for("add_race"))
@app.route("/races/<raceid>/delete", methods=['POST'])
@login_required(role="ADMIN")
def delete_race(raceid):

    race = Race.query.filter_by(raceid=raceid).first()
    if not race.isopen:
        Race.query.filter_by(raceid=raceid).delete()
        db.session().commit()

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



