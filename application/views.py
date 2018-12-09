from flask import render_template
from application import app, db
from sqlalchemy.sql import text

from application.search.forms import SearchForm
from application.drinks.models import Drink
from application.ingredients.models import Ingredient
from application.keywords.models import Keyword
from application.auth.models import User


@app.route("/")
def index():
    userStats = []
    stmt = text(" SELECT account.id, COUNT(account.id) as drinkCount"
                " FROM account"
                " LEFT JOIN drink ON drink.account_id = account.id"
                " WHERE (drink.accepted = 1)"
                " GROUP BY account.id"
                " HAVING COUNT(drink.id) > 0"
                " ORDER BY drinkCount DESC"
                " LIMIT 5")
    for row in db.engine.execute(stmt):
        user = User.query.get(row[0])
        userStats.append({'username': user.username, 'count': row[1]})

    stats = {
        "drinks": len(Drink.query.filter(Drink.accepted == 1).all()),
        "ingredients": len(Ingredient.query.filter(Ingredient.accepted == True).all()),
        "keywords": len(Keyword.query.filter(Keyword.accepted == True).all()),
        "userStats": userStats
    }
    return render_template("index.html", form=SearchForm(), stats=stats)
