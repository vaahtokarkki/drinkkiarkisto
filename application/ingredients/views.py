from application import app, db, login_required
from flask import render_template, request, url_for, redirect
from flask_login import current_user

from application.ingredients.models import Ingredient
from application.ingredients.forms import NewIngredientForm


@app.route("/ingredients", methods=["GET"])
def ingredients_index():
    return render_template("ingredients/list.html", ingredients=Ingredient.query.filter(Ingredient.accepted=='1'))

@app.route("/ingredients/new/")
@login_required(role="ANY")
def ingredients_form():
    return render_template("ingredients/new.html", form=NewIngredientForm())


@app.route("/ingredients/", methods=["POST"])
@login_required(role="ANY")
def ingredients_create():
    form = NewIngredientForm(request.form)

    if not form.validate():
        return render_template("ingredients/new.html", form=form)

    i = Ingredient(form.name.data, form.unit.data)

    if current_user is not None:
        i.account_id = current_user.id
        if current_user.role.name == "USER+" or current_user.role.name == "ADMIN":
            i.accepted = True

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/edit/<ingredient_id>/", methods=["GET"])
@login_required(role="ANY")
def ingredients_edit(ingredient_id):
    ingredient = Ingredient.query.get(ingredient_id)
    
    form = NewIngredientForm()
    form.name.data = ingredient.name
    form.unit.data = ingredient.unit
    
    return render_template("ingredients/edit.html", form=form, ingredient=ingredient)

@app.route("/ingredients/edit/<ingredient_id>/", methods=["POST"])
@login_required(role=3)
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
@login_required(role=3)
def ingredients_delete(ingredient_id):
    ingredient = Ingredient.query.get(ingredient_id)

    if ingredient is None:
        return redirect(url_for("ingredients_index"))
    
    db.session.delete(ingredient)
    db.session().commit()

    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/publish/<ingredient_id>", methods=["GET"])
@login_required(role=3)
def publish_ingredient(ingredient_id):
    i = Ingredient.query.get(ingredient_id)

    if not i:
        return redirect(url_for("admin_index"))
    
    i.accepted = True
    db.session().commit()

    return redirect(url_for("admin_index"))

@app.route("/ingredients/reject/<ingredient_id>", methods=["GET"])
@login_required(role=3)
def reject_ingredient(ingredient_id):
    i = Ingredient.query.get(ingredient_id)

    if not i:
        return redirect(url_for("admin_index"))
    
    db.session.delete(i)
    db.session().commit()

    return redirect(url_for("admin_index"))
