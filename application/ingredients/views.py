from application import app, db
from flask import render_template, request, url_for, redirect
from application.ingredients.models import Ingredient


@app.route("/ingredients", methods=["GET"])
def ingredients_index():
    return render_template("ingredients/list.html", ingredients=Ingredient.query.all())


@app.route("/ingredients/new/")
def ingredients_form():
    return render_template("ingredients/new.html")


@app.route("/ingredients/", methods=["POST"])
def ingredients_create():
    form = request.form
    i = Ingredient(form.get("name"), form.get("unit"))

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/edit/<ingredient_id>/", methods=["GET"])
def ingredients_edit(ingredient_id):
    k = Ingredient.query.get(ingredient_id)
    return render_template("ingredients/edit.html", ingredient=k)

@app.route("/ingredients/edit/<ingredient_id>/", methods=["POST"])
def ingredients_save_edit(ingredient_id):
    k = Ingredient.query.get(ingredient_id)

    k.name = request.form.get("name")
    k.unit = request.form.get("unit")

    db.session().commit()

    return redirect(url_for("ingredients_index"))