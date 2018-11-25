from application import app, db
from flask import render_template, request, url_for, redirect
from sqlalchemy.sql import text

from application.drinks.models import Drink
from application.ingredients.models import Ingredient
from application.keywords.models import Keyword
from application.search.forms import SearchForm

@app.route("/search",methods=["GET"])
def search_drinks():
    form = SearchForm(request.args)
    
    #Search by ingredient
    if form.ingredient.data:
        id = form.ingredient.data
        name = Ingredient.query.get(id)
        if name is not None:
            name = name.name
        
        stmt = text(" SELECT drink.name, drink.id"
                    " FROM drink"
                    " JOIN drink_ingredient ON drink_ingredient.drink_id = drink.id"
                    " JOIN ingredient ON ingredient.id = drink_ingredient.ingredient_id"
                    " AND ingredient.id == :id").params(id=id)
        res = list(db.engine.execute(stmt))
        return render_template("search/results.html", results=res, query=name)

    #Search by keyword
    if form.keyword.data:
        id = form.keyword.data
        name = Keyword.query.get(id)
        if name is not None:
            name = name.name
        
        res = list(Drink.query.filter(Drink.tags.any(Keyword.id == id)))
        return render_template("search/results.html", results=res, query=name)
        

    #TODO: Extend search to instructions
    byName = list(Drink.query.filter(Drink.name.contains(form.query.data)))
    byIngredient = list(Drink.query.filter(Drink.ingredients.any(Ingredient.name.contains(form.query.data))))
    byKeyword = list(Drink.query.filter(Drink.tags.any(Keyword.name.contains(form.query.data))))

    combinedResults = list(set(byName + byIngredient + byKeyword))
    return render_template("search/results.html", results=combinedResults, query=form.query.data)