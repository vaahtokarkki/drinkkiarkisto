from application import db
from application.models import Base

class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    roles = db.Column(db.Integer, db.ForeignKey('role.id'))
    
    drinks = db.relationship("Drink", backref='account', lazy=True)
    ingredients = db.relationship("Ingredient", backref='account', lazy=True)
    keywords = db.relationship("Keyword", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.roles = 1
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
