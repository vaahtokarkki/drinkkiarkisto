from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SearchForm(FlaskForm):
    query = StringField("Hae drinkkejä",[validators.Length(min=2, message=(u'Hakusanan olatava vähintään 2 merkkiä pitkä'))], render_kw={"placeholder":"Hakusana"})