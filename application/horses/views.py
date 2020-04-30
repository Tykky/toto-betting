from flask import render_template, request, url_for, redirect
from application import app, login_required, db
from application.horses.models import Horse
from application.horses.form import AddHorseForm

@app.route("/horses", methods=['GET'])
def horses():
    horses = Horse.query.all()
    return render_template("/horses/horses.html", horses = horses)

@app.route("/horses/add", methods=['GET','POST'])
@login_required(role="ADMIN")
def add_horse():
    if request.method == "GET":
        horses = Horse.query.all()
        return render_template("/horses/add.html", horses = horses, form=AddHorseForm())
        
    form = AddHorseForm(request.form)
    horse = Horse(form.name.data, form.breed.data, form.tier.data, form.description.data)
    db.session().add(horse)
    db.session().commit()

    return redirect(url_for('add_horse'))

@app.route("/horses/<horseid>/delete", methods=['POST'])
@login_required(role="ADMIN")
def delete_horse(horseid):
    horse = Horse.query.filter_by(horseid=horseid)
    races = Horse.races
    if horse.first():
        if not races:
            horse.delete()
            db.session().commit()
        else:
            horses = Horse.query.all()
            return render_template("/horses/add.html", horses=horses, form=AddHorseForm(),
            error=horse.first().name+" is attending in at least one of the races! Please remove "+horse.first().name+" from "+
            "all of the races before using delete.")
    return redirect(url_for('add_horse'))

@app.route("/horses/<horseid>/edit", methods=['POST','GET'])
@login_required(role="ADMIN")
def edit_horse(horseid):
    if request.method == 'GET':
        horse = Horse.query.get(horseid)
        if horse:
            form = AddHorseForm(name=horse.name, breed=horse.breed, tier=horse.tier,
            description=horse.description)
        else:
            form = AddHorseForm()

        return render_template("/horses/edit.html", form=form)