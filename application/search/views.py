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

    results = Drink.query.filter(Drink.accepted == '1').filter(
        Drink.name.contains(form.query.data) |
        Drink.instructions.contains(form.query.data) |
        Drink.ingredients.any(Ingredient.name.contains(form.query.data)) |
        Drink.tags.any(Keyword.name.contains(form.query.data))
        ).all()

    return render_template("search/results.html", results=results, query=form.query.data)