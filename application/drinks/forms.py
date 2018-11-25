from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, HiddenField, IntegerField,validators, TextAreaField
from wtforms.widgets import ListWidget, CheckboxInput

from application.ingredients.models import Ingredient
from application.keywords.models import Keyword

class MultiCheckboxField(SelectMultipleField):
    widget			= ListWidget(prefix_label=False)
    option_widget	= CheckboxInput()

class NewDrinkForm(FlaskForm):
    def generateSelectOptions():
        ingredientsList = Ingredient.query.all()
        print("mitä")
        ingredientPairs = []
        for i in ingredientsList:
            ingredientPairs.append((i.id, i.name+" ("+i.unit+")"))
        return ingredientPairs
    
    name = StringField("Drinkin nimi")
    amount = IntegerField("Määrä")
    instructions = TextAreaField("Valmistusohjeet")

    ingredientsAmount = HiddenField(default=0)

    ingredients = SelectField('Ainesosat',
                              choices=generateSelectOptions())
    
    keywordPairs = []
    for k in Keyword.query.all():
        keywordPairs.append((k.id, k.name))
    keywords = MultiCheckboxField('Avainsanat',choices=keywordPairs)

    class Meta:
        csrf = False

class EditDrink(FlaskForm):
    name = StringField("Drinkin nimi",[validators.Length(min=2,max=20, message=(u'Nimen olatava vähintään 2 merkkiä ja enintään 20 merkkiä pitkä'))])
    instructions = TextAreaField("Valmistusohjeet")

