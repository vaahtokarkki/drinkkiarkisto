from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewKeywordForm(FlaskForm):
    name = StringField("Avainsanan nimi",[validators.Length(min=2,max=20, message=(u'Nimen olatava vähintään 2 merkkiä ja enintään 20 merkkiä pitkä'))], render_kw={"placeholder":"Avainsana"})
    
    class Meta:
        csrf = False