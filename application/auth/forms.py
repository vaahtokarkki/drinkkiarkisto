from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi",[validators.Length(min=2)],render_kw={"placeholder": "Käyttäjänimi"})
    password = PasswordField("Salasana",[validators.Length(min=6)], render_kw={"placeholder": "Salasana"})
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=5)], render_kw={"placeholder": "Nimi"})
    username = StringField("Käyttäjänimi",[validators.Length(min=2)],render_kw={"placeholder": "Käyttäjänimi"})
    password = PasswordField("Salasana",[validators.Length(min=6)], render_kw={"placeholder": "Salasana"})
    passwordAgain = PasswordField("Salasana uudestaan",[validators.Length(min=6)], render_kw={"placeholder": "Salasana uudestaan"})

    class Meta:
        csrf = False