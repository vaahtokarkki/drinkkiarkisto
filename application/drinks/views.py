from application import app, db
from flask import render_template, request, url_for, redirect

from application.drinks.models import Drink
from application.drinks.forms import NewDrinkForm
from application.keywords.models import Keyword
from application.ingredients.models import Ingredient


@app.route("/drinks", methods=["GET"])
def drinks_index():
    return render_template("drinks/list.html", drinks=Drink.query.all())


@app.route("/drinks/<drink_id>", methods=["GET"])
def get_drink(drink_id):
    return render_template("drinks/drink.html", drink=Drink.query.get(drink_id))


@app.route("/drinks/new/")
def drinks_form():
    return render_template("drinks/new.html", form=NewDrinkForm(), ingredients=Ingredient.query.all(), keywords=Keyword.query.all())


@app.route("/drinks/", methods=["POST"])
def drinks_create():
    form = NewDrinkForm(request.form)

    if not form.validate():
        return render_template("drinks/new.html", form=form, ingredients=Ingredient.query.all(), keywords=Keyword.query.all())

    d = Drink(form.name.data)
    ingredientAmount = int(form.ingredientsAmount.data)

    for i in range(0, ingredientAmount+1):
        if i is 0:
            ingredient = Ingredient.query.get(form.ingredients.data)
            d.ingredients.append(ingredient)
            continue
        id = request.form.get("ingredients-"+str(i))
        ingredient = Ingredient.query.get(id)
        
        if ingredient in d.ingredients:
            continue
        d.ingredients.append(ingredient)

    for id in form.keywords.data:
        k = Keyword.query.get(id)
        d.tags.append(k)

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


@app.route("/drinks/delete/<drink_id>/", methods=["GET"])
def drinks_delete(drink_id):
    d = Drink.query.get(drink_id)

    if d is None:
        return redirect(url_for("drinks_index"))

    db.session.delete(d)
    db.session().commit()
    return redirect(url_for("drinks_index"))