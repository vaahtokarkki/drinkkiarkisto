from application import app, db
from flask import render_template, request, url_for, redirect
from application.keywords.models import Keyword


@app.route("/keywords", methods=["GET"])
def keywords_index():
    return render_template("keywords/list.html", keywords=Keyword.query.all())


@app.route("/keywords/new/")
def keywords_form():
    return render_template("keywords/new.html")


@app.route("/keywords/", methods=["POST"])
def keywords_create():
    k = Keyword(request.form.get("name"))

    db.session().add(k)
    db.session().commit()

    return redirect(url_for("keywords_index"))

@app.route("/keywords/edit/<keyword_id>/", methods=["GET"])
def keywords_edit(keyword_id):
    k = Keyword.query.get(keyword_id)
    return render_template("keywords/edit.html", keyword=k)

@app.route("/keywords/edit/<keyword_id>/", methods=["POST"])
def keywords_save_edit(keyword_id):
    k = Keyword.query.get(keyword_id)

    k.name = request.form.get("name")

    db.session().commit()

    return redirect(url_for("keywords_index"))
