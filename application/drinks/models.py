from application import db
from application.models import Base

keywords = db.Table('keywords_helper',
                    db.Column('keyword_id', db.Integer, db.ForeignKey(
                        'keyword.id'), primary_key=True),
                    db.Column('drink_id', db.Integer, db.ForeignKey(
                        'drink.id'), primary_key=True)
                    )

ingredientsTable = db.Table('ingredients_helper',
                            db.Column('ingredient_id', db.Integer, db.ForeignKey(
                                'ingredient.id'), primary_key=True),
                            db.Column('drink_id', db.Integer, db.ForeignKey(
                                'drink.id'), primary_key=True)
                            )


class Drink(Base):
    __tablename__ = "drink"

    tags = db.relationship('Keyword', secondary=keywords,
                           backref=db.backref('keywords_helper', lazy=True,load_on_pending=False))

    ingredients = db.relationship('Ingredient', secondary=ingredientsTable,
                                  backref=db.backref('ingredients_helper', lazy=True,load_on_pending=False))

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
