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
    Horse.query.filter_by(horseid=horseid).delete()
    db.session().commit()
    
    return redirect(url_for('add_horse'))