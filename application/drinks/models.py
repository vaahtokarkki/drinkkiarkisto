from application import db
from application.models import Base
from application.ingredients.models import Ingredient
from application.auth.models import User

keywords = db.Table('keywords_helper',
                    db.Column('keyword_id', db.Integer, db.ForeignKey(
                        'keyword.id'), primary_key=True),
                    db.Column('drink_id', db.Integer, db.ForeignKey(
                        'drink.id'), primary_key=True)
                    )

class Drink(Base):
    __tablename__ = "drink"

    tags = db.relationship('Keyword', secondary=keywords,
                           backref=db.backref('keywords_helper', lazy=True, load_on_pending=False))
    ingredients = db.relationship('DrinkIngredient', back_populates='drink')
    
    name = db.Column(db.String(50), nullable=False)
    instructions = db.Column(db.String(250))
    accepted = db.Column(db.Boolean, nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    user = db.relationship("User", back_populates="drinks")

    def __init__(self, name):
        self.name = name
        self.accepted = False

class DrinkIngredient(Base):
    __tablename__ = 'drink_ingredient'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    drink_id = db.Column(db.Integer, db.ForeignKey(Drink.id))
    ingredient_id = db.Column(db.Integer, db.ForeignKey(Ingredient.id))

    drink = db.relationship('Drink', back_populates='ingredients')
    ingredient = db.relationship('Ingredient', back_populates='drink')