from application import app, db
from flask import render_template

from application.auth.models import User


@app.route("/profile/<profile_id>", methods=["GET"])
def view_profile(profile_id):
    error = None
    p = User.query.get(profile_id)
    
    if not p:
        error ="Käyttäjätunnusta ei löytynyt."
        return render_template("profile/view.html", user=None, errors=error)
    
    return render_template("profile/view.html", user=p, errors=error)