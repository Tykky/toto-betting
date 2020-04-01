from flask import render_template, request, redirect, url_for
from application import app, login_required, db
from application.races.forms import AddRaceForm
from application.races.models import Race

@app.route("/races/add", methods=['GET','POST'])
@login_required(role="ADMIN")
def add_race():
    if request.method == "GET":
        return render_template("/races/add.html", form = AddRaceForm())

    form = AddRaceForm(request.form)
    race = Race(form.name.data, form.location.data, form.description.data)

    db.session().add(race)
    db.session().commit()

    return redirect(url_for("add_race"))


