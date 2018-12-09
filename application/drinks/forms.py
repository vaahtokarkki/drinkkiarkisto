from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, HiddenField, DecimalField,validators, TextAreaField
from wtforms.widgets import ListWidget, CheckboxInput

from application.ingredients.models import Ingredient
from application.keywords.models import Keyword

class MultiCheckboxField(SelectMultipleField):
    widget			= ListWidget(prefix_label=False)
    option_widget	= CheckboxInput()

class NewDrinkForm(FlaskForm):
    def generateSelectOptions(): #Define function as workaround to get options visible on heroku... 
        #Ingredient.query.filter(Ingredient.accepted==False, Ingredient.account_id==current_user.id).all()
        ingredientsList = Ingredient.query.order_by(Ingredient.name).all()
        ingredientPairs = []
        for i in ingredientsList:
            ingredientPairs.append((i.id, i.name+" ("+i.unit+")"))
        return ingredientPairs
    
    def generateCheckboxOptions():
        keywordPairs = []
        for k in Keyword.query.all():
            keywordPairs.append((k.id, k.name))
        return keywordPairs

    name = StringField("Drinkin nimi")
    amount = StringField("Määrä") #Validointi numeroille tehdään views.py tiedostossa
    instructions = TextAreaField("Valmistusohjeet")

    ingredientsAmount = HiddenField(default=0)

    ingredients = SelectField('Ainesosat',
                              choices=generateSelectOptions())
    
    keywords = MultiCheckboxField('Avainsanat',choices=generateCheckboxOptions())

    class Meta:
        csrf = False

class EditDrink(FlaskForm):
    name = StringField("Drinkin nimi",[validators.Length(min=2,max=20, message=(u'Nimen olatava vähintään 2 merkkiä ja enintään 20 merkkiä pitkä'))])
    instructions = TextAreaField("Valmistusohjeet")