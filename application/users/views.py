from application import app, db
from flask import redirect, render_template, request, url_for
from application.users.models import User

@app.route("/users", methods=["GET"])
def users_index():
    return render_template("users/list.html", users = User.query.all())

@app.route("/users/new")
def user_form():
    return render_template("users/new.html")

@app.route("/users/edit")
def user_edit():
    return render_template("users/edit.html")

@app.route("/users/<user_id>", methods=["POST"])
def user_set_credits(user_id):

    u = User.query.get(user_id)
    u.credits = request.form.get("credits")
    if not u:
        db.session().commit()

    return redirect(url_for('users_index'))

@app.route("/users", methods=["POST"])
def user_create():

    user = User(request.form.get("name"))

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("users_index"))