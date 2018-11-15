from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, HiddenField 
from wtforms.widgets import ListWidget, CheckboxInput

from application.ingredients.models import Ingredient
from application.keywords.models import Keyword


class MultiCheckboxField(SelectMultipleField):
    widget			= ListWidget(prefix_label=False)
    option_widget	= CheckboxInput()

class NewDrinkForm(FlaskForm):
    name = StringField("Drinkin nimi")

    amount = StringField("Määrä")
    #ingredient = StringField("Ainesosa")

    ingredientsAmount = HiddenField(default=0)
    #ingredientsAmount.default="1"

    ingredientsList = Ingredient.query.all()
    ingredientPairs = []
    for i in ingredientsList:
        ingredientPairs.append((i.id, i.name+" ("+i.unit+")"))
    ingredients = SelectField('Ainesosat',
                              choices=ingredientPairs)

    keywordPairs = []
    for k in Keyword.query.all():
        keywordPairs.append((k.id, k.name))
    keywords = MultiCheckboxField('Avainsanat',choices=keywordPairs)

    class Meta:
        csrf = False
