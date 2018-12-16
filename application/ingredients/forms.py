from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewIngredientForm(FlaskForm):
    name = StringField("Ainesosan nimi",[validators.Length(min=2,max=20, message=(u'Nimen oltava vähintään 2 merkkiä ja enintään 20 merkkiä pitkä'))], render_kw={"placeholder":"Nimi"})
    unit = StringField("Yksikkö",[validators.Length(max=20, message=(u'Nimen oltava enintään 20 merkkiä pitkä'))], render_kw={"placeholder":"esim. Kpl"})
    
    class Meta:
        csrf = False