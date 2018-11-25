from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required

from application.drinks.models import Drink, DrinkIngredient
from application.drinks.forms import NewDrinkForm, EditDrink
from application.keywords.models import Keyword
from application.ingredients.models import Ingredient


@app.route("/drinks", methods=["GET"])
def drinks_index():
    return render_template("drinks/list.html", drinks=Drink.query.all())

@app.route("/drinks/<drink_id>", methods=["GET"])
def get_drink(drink_id):
    return render_template("drinks/drink.html", drink=Drink.query.get(drink_id))


@app.route("/drinks/new/")
@login_required
def drinks_form():
    return render_template("drinks/new.html", form=NewDrinkForm(), ingredients=Ingredient.query.all(), keywords=Keyword.query.all())

@app.route("/drinks/", methods=["POST"])
@login_required
def drinks_create():
    form = NewDrinkForm(request.form)

    valid = True
    name = form.name.data
    instructions = form.instructions.data

    if len(name) < 2 or len(name) > 20:
        form.name.errors = list(form.name.errors)
        form.name.errors.append("Nimen oltava vähintään 2 merkkiä ja enintään 20 merkkiä ptkä")
        valid = False

    if len(instructions) > 200:
        form.instructions.errors = list(form.instructions.errors)
        form.instructions.errors.append("Ohje saa olla enintään 200 merkkiä pitkä")
        valid = False

    
    d = Drink(name)
    d.instructions = instructions
    ingredientAmount = int(form.ingredientsAmount.data)
    
    for i in range(0, ingredientAmount+1):
        if i is 0:
            ingredient = Ingredient.query.get(form.ingredients.data)
            if ingredient is None:
                continue

            try:
                amount = int(form.amount.data)
            except:
                form.ingredientError = ["Ainesosien määrät täytyvät olla numeroita"] 
                valid = False
                continue
                
            DrinkIngredient(drink=d, ingredient=ingredient, amount=amount)
            continue
        
        id = request.form.get("ingredients-"+str(i))
        ingredient = Ingredient.query.get(id)
        try:
            amount = int(request.form.get("amount-"+str(i)))
        except:
            form.ingredientError = ["Ainesosien määrät täytyvät olla numeroita"]
            valid = False
            continue
        
        if ingredient is None or ingredient in d.ingredients:
            continue

        DrinkIngredient(drink=d, ingredient=ingredient, amount=amount)

    if not valid:
        return render_template("drinks/new.html", form=form, ingredients=Ingredient.query.all(), keywords=Keyword.query.all())

    for id in form.keywords.data:
        k = Keyword.query.get(id)
        d.tags.append(k)

    if current_user is not None:
        d.account_id = current_user.id

    db.session().add(d)
    db.session().commit()

    return redirect(url_for("drinks_index"))


@app.route("/drinks/edit/<drink_id>/", methods=["GET"])
@login_required
def drinks_edit(drink_id):
    d = Drink.query.get(drink_id)
    form = EditDrink()
    form.name.data = d.name
    form.instructions.data = d.instructions

    return render_template("drinks/edit.html", drink=d, form=form)


@app.route("/drinks/edit/<drink_id>/", methods=["POST"])
@login_required
def drinks_save_edit(drink_id):
    form = EditDrink(request.form)
    d = Drink.query.get(drink_id)

    valid = True
    name = form.name.data
    instructions = form.instructions.data

    if len(name) < 2 or len(name) > 20:
        form.name.errors = list(form.name.errors)
        form.name.errors.append("Nimen oltava vähintään 2 merkkiä ja enintään 20 merkkiä ptkä")
        valid = False

    if len(instructions) > 200:
        form.instructions.errors = list(form.instructions.errors)
        form.instructions.errors.append("Ohje saa olla enintään 200 merkkiä pitkä")
        valid = False

    for i in range(1,len(d.ingredients)+1):
        try:
            amount = int(request.form.get("amount-"+str(i)))
        except:
            form.ingredientError = ["Ainesosien määrät täytyvät olla numeroita"]
            valid = False
            continue

        d.ingredients[i-1].amount = amount

    if not valid:
        return render_template("drinks/edit.html", form=form, drink=d)

    d.name = form.name.data
    d.instructions = form.instructions.data

    db.session().commit()
    return redirect(url_for("drinks_index"))


@app.route("/drinks/delete/<drink_id>/", methods=["GET"])
@login_required
def drinks_delete(drink_id):
    d = Drink.query.get(drink_id)

    if d is None:
        return redirect(url_for("drinks_index"))

    db.session.delete(d)
    db.session().commit()
    return redirect(url_for("drinks_index"))

def getDrinksCount():
    return Drink.query.all().count()