from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()

    if not user or not bcrypt.check_password_hash(user.phash, form.password.data):
        return render_template("auth/loginform.html", form = form,
                               error = "Invalid username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods= ["GET", "POST"])
def auth_register():
    if(request.method == "GET"):
        return render_template("auth/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    if not form.password1.data == form.password2.data:
        form.password1.errors.append("Passwords do not match")
        form.password2.errors.append("Passwords do not match")
        return render_template("auth/registerform.html", form = form)

    if User.query.filter_by(username=form.username.data).first():
        form.username.errors.append("Username already taken")
        return render_template("auth/registerform.html", form = form)

    phash = bcrypt.generate_password_hash(form.password1.data)
    print("---PRINT PASSWORD HASH---")
    print(phash)
    print("--END PASSWORD HASH---")
    user = User(form.username.data, phash)

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("index"))



    



