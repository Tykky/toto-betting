from flask import render_template, request, redirect, url_for
from application import app, login_required, db
from application.races.forms import AddRaceForm
from application.races.models import Race

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

    Race.query.filter_by(raceid=raceid).delete()
    db.session().commit()

    return redirect(url_for('add_race'))
