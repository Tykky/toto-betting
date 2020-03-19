from application import app, db
from flask import redirect, render_template, request, url_for
from application.users.models import User

@app.route("/tasks", methods=["GET"])
def users_index():
    return render_template("users/list.html", users = User.query.all())

@app.route("/users/new")
def user_form():
    return render_template("users/new.html")

@app.route("/users", methods=["POST"])
def user_create():

    user = User(request.form.get("name"))

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("users_index"))