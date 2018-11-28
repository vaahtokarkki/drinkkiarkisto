from application import app, db, login_required
from flask import render_template

from application.drinks.models import Drink

@app.route("/admin", methods=["GET"])
@login_required(role=3)
def admin_index():

    return render_template("admin/index.html")