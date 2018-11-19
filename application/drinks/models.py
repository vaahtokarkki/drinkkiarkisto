from application import db
from application.models import Base
from application.ingredients.models import Ingredient

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
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

class DrinkIngredient(Base):
    __tablename__ = 'drink_ingredient'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    drink_id = db.Column(db.Integer, db.ForeignKey(Drink.id))
    ingredient_id = db.Column(db.Integer, db.ForeignKey(Ingredient.id))

    drink = db.relationship('Drink', back_populates='ingredients')
    ingredient = db.relationship('Ingredient', back_populates='drink')