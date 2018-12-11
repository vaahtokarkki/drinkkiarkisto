from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators

from application.auth.role import Role
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi",[validators.Length(min=2, max=20)],render_kw={"placeholder": "Käyttäjänimi"})
    password = PasswordField("Salasana",[validators.Length(min=5, max=20)], render_kw={"placeholder": "Salasana"})
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=5, max=20)], render_kw={"placeholder": "Nimi"})
    username = StringField("Käyttäjänimi",[validators.Length(min=2, max=20)],render_kw={"placeholder": "Käyttäjänimi"})
    password = PasswordField("Salasana",[validators.Length(min=6, max=30)], render_kw={"placeholder": "Salasana"})
    passwordAgain = PasswordField("Salasana uudestaan",[validators.Length(min=6, max=30)], render_kw={"placeholder": "Salasana uudestaan"})

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=5, max=20)], render_kw={"placeholder": "Nimi"})
    username = StringField("Käyttäjänimi",[validators.Length(min=2, max=20)],render_kw={"placeholder": "Käyttäjänimi"})
    
    def generateSelectOptions(): #Define function as workaround to get options visible on heroku... 
        rolesList = Role.query.all()
        ingredientPairs = []
        for i in rolesList:
            ingredientPairs.append((str(i.id), str(i.displayName)))
        return ingredientPairs
    
    roles = SelectField('Rooli', choices=generateSelectOptions())

    class Meta:
        csrf = False