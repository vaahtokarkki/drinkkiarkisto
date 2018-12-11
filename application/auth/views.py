from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    print("Käyttäjä " + user.name + " tunnistettiin")
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods=["GET"])
def auth_register_form():
    return render_template("auth/register.html", form=RegisterForm())

@app.route("/auth/register", methods=["POST"])
def auth_register():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/register.html", form=form)

    if form.password.data != form.passwordAgain.data:
        form.password.errors.append("Salasanat eivät täsmää")
        return render_template("auth/register.html", form=form)

    checkUser = User.query.filter(User.username == form.username.data).first()
    if checkUser:
        form.username.errors.append("Käyttäjänimi varattu")
        return render_template("auth/register.html", form=form)

    user = User(form.name.data, form.username.data, form.password.data)

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("auth_login"))