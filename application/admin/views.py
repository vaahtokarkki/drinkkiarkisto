from application import app, db, login_required
from flask import render_template

from application.drinks.models import Drink
from application.ingredients.models import Ingredient
from application.keywords.models import Keyword
from application.auth.models import User


@app.route("/admin", methods=["GET"])
@login_required(role=3)
def admin_index():
    drinks =[]
    drinks = Drink.query.filter(Drink.accepted == False)
    ingredients = Ingredient.query.filter(Ingredient.accepted == False)
    keywords = Keyword.query.filter(Keyword.accepted == False)
    print("jee")
    print(drinks)
    return render_template("admin/index.html", waitingDrinks=drinks, waitingIngredients=ingredients, waitingKeywords=keywords)


@app.route("/admin/users", methods=["GET"])
@login_required(role=3)
def list_users():
    return render_template("admin/users.html", users=User.query.all())
