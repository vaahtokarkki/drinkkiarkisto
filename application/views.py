from flask import render_template
from application import app

from application.search.forms import SearchForm
from application.drinks.models import Drink
from application.ingredients.models import Ingredient
from application.keywords.models import Keyword

@app.route("/")
def index():
    stats = {
        "drinks": len(Drink.query.filter(Drink.accepted==True).all()),
        "ingredients": len(Ingredient.query.filter(Ingredient.accepted==True).all()),
        "keywords": len(Keyword.query.filter(Keyword.accepted==True).all())
    }
    return render_template("index.html", form=SearchForm(), stats=stats)