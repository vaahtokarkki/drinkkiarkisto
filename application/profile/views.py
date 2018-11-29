from application import app, db, login_required
from flask import render_template
from flask_login import current_user

from application.auth.models import User
from application.auth.forms import EditForm

@app.route("/profile/<profile_id>", methods=["GET"])
def view_profile(profile_id):
    error = None
    p = User.query.get(profile_id)
    
    if not p:
        error ="Käyttäjätunnusta ei löytynyt."
        return render_template("profile/view.html", user=None, errors=error)
    
    return render_template("profile/view.html", user=p, errors=error)

@app.route("/profile/edit/<profile_id>", methods=["GET"])
@login_required(role="ANY")
def edit_user(profile_id):
    user = User.query.get(profile_id)

    if not user:
        error = "Profiilia ei löytynyt"
        return render_template("profile/edit.html", authError=error)

    if (current_user.id != user.id and current_user.role.name != "ADMIN") or current_user.role.name is "ADMIN":
        error = "Voit muokata vain omaa profiilia"
        return render_template("profile/edit.html", authError=error)
    
    form = EditForm()

    form.name.data = user.name
    form.username.data = user.username

    return render_template("profile/edit.html", form=form, profile=user)

@app.route("/profile/edit/<profile_id>", methods=["GET"])
@login_required(role="ANY")
def edit_user_save(profile_id):
    return None
