from application import app, db
from flask import render_template, request, url_for, redirect

from application.drinks.models import Drink
from application.search.forms import SearchForm

@app.route("/search",methods=["GET"])
def search_drinks():
    form = SearchForm(request.args)
    results = Drink.query.filter(Drink.name.contains(form.query.data))

    return render_template("search/results.html", results=results)
    ##results = Drink.query.filter(Drink.name)