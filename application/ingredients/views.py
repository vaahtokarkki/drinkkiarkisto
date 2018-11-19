from application import app, db
from flask import render_template, request, url_for, redirect

from application.ingredients.models import Ingredient
from application.ingredients.forms import NewIngredientForm


@app.route("/ingredients", methods=["GET"])
def ingredients_index():
    return render_template("ingredients/list.html", ingredients=Ingredient.query.all())


@app.route("/ingredients/new/")
def ingredients_form():
    return render_template("ingredients/new.html", form=NewIngredientForm())


@app.route("/ingredients/", methods=["POST"])
def ingredients_create():
    form = NewIngredientForm(request.form)

    if not form.validate():
        return render_template("ingredients/new.html", form=form)

    i = Ingredient(form.name.data, form.unit.data)

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/edit/<ingredient_id>/", methods=["GET"])
def ingredients_edit(ingredient_id):
    ingredient = Ingredient.query.get(ingredient_id)
    
    form = NewIngredientForm()
    form.name.data = ingredient.name
    form.unit.data = ingredient.unit
    
    return render_template("ingredients/edit.html", form=form, ingredient=ingredient)

@app.route("/ingredients/edit/<ingredient_id>/", methods=["POST"])
def ingredients_save_edit(ingredient_id):
    form = NewIngredientForm(request.form)
    ingredient = Ingredient.query.get(ingredient_id)

    if not form.validate():
        return render_template("ingredients/edit.html", form=form, ingredient=ingredient)

    ingredient.name = form.name.data
    ingredient.unit = form.unit.data

    db.session().commit()

    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/delete/<ingredient_id>/", methods=["GET"])
def ingredients_delete(ingredient_id):
    ingredient = Ingredient.query.get(ingredient_id)

    if ingredient is None:
        return redirect(url_for("ingredients_index"))
    
    db.session.delete(ingredient)
    db.session().commit()

    return redirect(url_for("ingredients_index"))