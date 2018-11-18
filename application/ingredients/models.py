from application import db

class Ingredient(db.Model):
    __tablename__ = "ingredient"
    
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    unit = db.Column(db.String(10))

    def __init__(self, name, unit):
        self.name = name
        self.unit = unit