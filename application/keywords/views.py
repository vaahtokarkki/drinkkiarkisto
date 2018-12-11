from application import app, db, login_required
from flask import render_template, request, url_for, redirect
from flask_login import current_user

from application.keywords.models import Keyword
from application.keywords.forms import NewKeywordForm


@app.route("/keywords", methods=["GET"])
def keywords_index():
    page = request.args.get('page', 1, type=int)
    keywords = Keyword.query.filter(Keyword.accepted == '1').order_by(
        Keyword.name).paginate(page, 5, False)
    next_url = url_for('keywords_index', page=keywords.next_num) \
        if keywords.has_next else None
    prev_url = url_for('keywords_index', page=keywords.prev_num) \
        if keywords.has_prev else None
    return render_template("keywords/list.html", keywords=keywords, next_url=next_url, prev_url=prev_url, current=page)


@app.route("/keywords/new/")
@login_required(role="ANY")
def keywords_form():
    return render_template("keywords/new.html", form=NewKeywordForm())


@app.route("/keywords/", methods=["POST"])
@login_required(role="ANY")
def keywords_create():
    form = NewKeywordForm(request.form)

    if not form.validate():
        return render_template("keywords/new.html", form=form)

    name = str(form.name.data).capitalize()
    k = Keyword(name)

    if current_user is not None:
        k.account_id = current_user.id
        if current_user.role.name == "USER+" or current_user.role.name == "ADMIN":
            k.accepted = True

    db.session().add(k)
    db.session().commit()

    return redirect(url_for("keywords_index"))


@app.route("/keywords/edit/<keyword_id>/", methods=["GET"])
@login_required(role=3)
def keywords_edit(keyword_id):
    k = Keyword.query.get(keyword_id)

    form = NewKeywordForm()
    form.name.data = k.name
    return render_template("keywords/edit.html", form=form, keyword=k)


@app.route("/keywords/edit/<keyword_id>/", methods=["POST"])
@login_required(role=3)
def keywords_save_edit(keyword_id):
    form = NewKeywordForm(request.form)
    k = Keyword.query.get(keyword_id)

    if not form.validate():
        return render_template("keywords/edit.html", form=form, keyword=k)

    k.name = form.name.data

    db.session().commit()

    return redirect(url_for("keywords_index"))


@app.route("/keywords/delete/<keyword_id>/", methods=["GET"])
@login_required(role=3)
def keywords_delete(keyword_id):
    keyword = Keyword.query.get(keyword_id)

    if keyword is None:
        return redirect(url_for("keywords_index"))

    db.session.delete(keyword)
    db.session().commit()

    return redirect(url_for("keywords_index"))


@app.route("/keywords/publish/<keyword_id>", methods=["GET"])
@login_required(role=3)
def publish_keyword(keyword_id):
    k = Keyword.query.get(keyword_id)

    if k is None:
        return redirect(url_for("admin_index"))

    k.accepted = True
    db.session().commit()

    return redirect(url_for("admin_index"))

#Oma funktio vaikka sama, kuin keywords_delete, mutta return-osoite eri.
@app.route("/keywords/reject/<keyword_id>", methods=["GET"])
@login_required(role=3)
def reject_keyword(keyword_id):
    k = Keyword.query.get(keyword_id)

    if k is None:
        return redirect(url_for("admin_index"))

    db.session.delete(k)
    db.session().commit()

    return redirect(url_for("admin_index"))
