from flask import render_template
from application import app

from application.search.forms import SearchForm

@app.route("/")
def index():
    return render_template("index.html", form=SearchForm())