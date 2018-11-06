from application import app, db
from flask import render_template, request, url_for, redirect
from application.drinks.models import Drink


@app.route("/drinks", methods=["GET"])
def drinks_index():
    return render_template("drinks/list.html", drinks=Drink.query.all())


@app.route("/drinks/new/")
def drinks_form():
    return render_template("drinks/new.html")


@app.route("/drinks/", methods=["POST"])
def drinks_create():
    d = Drink(request.form.get("name"))

    db.session().add(d)
    db.session().commit()

    return redirect(url_for("drinks_index"))

@app.route("/drinks/edit/<drink_id>/", methods=["GET"])
def drinks_edit(drink_id):
    d = Drink.query.get(drink_id)
    return render_template("drinks/edit.html", drink=d)

@app.route("/drinks/edit/<drink_id>/", methods=["POST"])
def drinks_save_edit(drink_id):
    d = Drink.query.get(drink_id)

    d.name = request.form.get("name")

    db.session().commit()

    return redirect(url_for("drinks_index"))
