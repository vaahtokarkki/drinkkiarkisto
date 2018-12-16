from application import app, db
from flask import render_template, request, url_for, redirect
from sqlalchemy.sql import text

from application.drinks.models import Drink
from application.ingredients.models import Ingredient
from application.keywords.models import Keyword
from application.search.forms import SearchForm


@app.route("/search", methods=["GET"])
def search_drinks():
    form = SearchForm(request.args)

    # Search by ingredient
    if form.ingredient.data:
        id = form.ingredient.data
        name = Ingredient.query.get(id)
        if name is not None:
            name = name.name

        stmt = text(" SELECT drink.name, drink.id"
                    " FROM drink"
                    " JOIN drink_ingredient ON drink_ingredient.drink_id = drink.id"
                    " JOIN ingredient ON ingredient.id = drink_ingredient.ingredient_id"
                    " AND drink.accepted = '1'"
                    " AND ingredient.id = :id").params(id=id)
        res = list(db.engine.execute(stmt))
        return render_template("search/results.html", results=res, query=name)

    # Search by keyword
    if form.keyword.data:
        id = form.keyword.data
        name = Keyword.query.get(id)
        if name is not None:
            name = name.name

        res = Drink.query.filter(
            Drink.accepted=='1',
            Drink.tags.any(Keyword.id == id),
            Drink.tags.any(Keyword.accepted == '1')
            ).all()
        return render_template("search/results.html", results=res, query=name)

    stmt = text("SELECT DISTINCT drink.id, drink.name FROM drink"
                " LEFT join drink_ingredient on drink_ingredient.drink_id = drink.id" 
                " LEFT join ingredient on ingredient.id = drink_ingredient.ingredient_id"
                " LEFT join keywords_helper on keywords_helper.drink_id = drink.id"
                " LEFT join keyword on keyword.id = keywords_helper.keyword_id"
                " WHERE drink.accepted = '1' and ("
                " LOWER(drink.name) LIKE LOWER(:query) or"
                " LOWER (drink.instructions) LIKE LOWER(:query) or"
                " LOWER(ingredient.name) LIKE LOWER(:query) or"
                " LOWER(keyword.name) LIKE LOWER(:query)"
                " )"
                " GROUP BY drink.id").params(query="%"+form.query.data+"%")
    res = list(db.engine.execute(stmt))

    return render_template("search/results.html", results=res, query=form.query.data)