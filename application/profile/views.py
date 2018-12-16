from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user, logout_user

from application.auth.models import User
from application.auth.forms import EditForm

@app.route("/profile/<profile_id>", methods=["GET"])
def view_profile(profile_id):
    try:
        int(profile_id)
    except:
        return render_template("profile/view.html", user=None)

    p = User.query.get(profile_id)

    if p is None:
        return render_template("profile/view.html", user=None)
    
    return render_template("profile/view.html", user=p)

@app.route("/profile/edit/<profile_id>", methods=["GET"])
@login_required(role="ANY")
def edit_user(profile_id):
    user = User.query.get(profile_id)
    if not user:
        error = "Profiilia ei löytynyt."
        return render_template("profile/edit.html", authError=error)

    if (current_user.id != user.id and current_user.role.name != "ADMIN") or current_user.role.name is "ADMIN":
        error = "Voit muokata vain omaa profiilia."
        return render_template("profile/edit.html", authError=error)
    
    form = EditForm(roles=user.role.id)

    form.name.data = user.name
    form.username.data = user.username

    return render_template("profile/edit.html", form=form, profile=user)

@app.route("/profile/edit/<profile_id>", methods=["POST"])
@login_required(role="ANY")
def edit_user_save(profile_id):
    form = EditForm(request.form)
    user = User.query.get(profile_id)

    if (current_user.id != user.id and current_user.role.name != "ADMIN") or current_user.role.name is "ADMIN":
        error = "Voit muokata vain omaa profiilia."
        return render_template("profile/edit.html", authError=error)
    
    if current_user.role.name != "ADMIN":
        form.roles.data = str(user.roles)

    if not form.validate():
        return render_template("profile/edit.html", form=form, profile=user)
    
    user.name = form.name.data
    user.username = form.username.data

    if form.newPassword.data:
        print("chaning password")
        if user.password != form.oldPassword.data:
            form.oldPassword.errors.append("Väärä salasana")
            return render_template("profile/edit.html", form=form, profile=user)

        if form.newPassword.data != form.newPasswordAgain.data:
            form.newPassword.errors.append("Salasanat eivät täsmää")
            return render_template("profile/edit.html", form=form, profile=user)

        user.password = form.newPassword.data

    if current_user.role.name == "ADMIN":
        user.roles = form.roles.data

    db.session().commit()

    return redirect(url_for('view_profile', profile_id=user.id))

@app.route("/profile/delete/<profile_id>", methods=["GET"])
@login_required(role="ANY")
def delete_user(profile_id):
    user = User.query.get(profile_id)

    if (current_user.id != user.id and current_user.role.name != "ADMIN") or current_user.role.name is "ADMIN":
        return redirect(url_for("index"))

    db.session.delete(user)
    db.session().commit()

    if current_user.role.name != "ADMIN":
        #Kirjaudu ulos jos käyttäjä poistaa oman profiilin
        logout_user()
        return redirect(url_for("index"))
    
    return redirect(url_for("list_users"))