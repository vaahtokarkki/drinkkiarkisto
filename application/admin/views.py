from application import app, db, login_required
from flask import render_template

from application.drinks.models import Drink
from application.auth.models import User

@app.route("/admin", methods=["GET"])
@login_required(role=3)
def admin_index():
    return render_template("admin/index.html", waitingDrinks=Drink.query.filter(Drink.accepted==False))

@app.route("/admin/users", methods=["GET"])
@login_required(role=3)
def list_users():
    return render_template("admin/users.html", users=User.query.all())