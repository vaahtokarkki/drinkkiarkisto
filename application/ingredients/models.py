from application import db
from application.models import Base

class Ingredient(Base):
    __tablename__ = "ingredient"
    
    name = db.Column(db.String(144), nullable=False)
    unit = db.Column(db.String(10))

    drink = db.relationship('DrinkIngredient', back_populates='ingredient')


    def __init__(self, name, unit):
        self.name = name
        self.unit = unit