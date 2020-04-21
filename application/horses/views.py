from flask import render_template, request
from application import app, login_required
from application.horses.models import Horse

@app.route("/horses", methods=['GET'])
def horses():
    horses = Horse.query.all()
    return render_template("/horses/horses.html", horses = horses)


@app.route("/horses/add", methods=['GET','POST'])
@login_required(role="ADMIN")
def add_horses():
    horses = Horse.query.all()
    return render_template("/horses/add.html", horses = horses)
    


