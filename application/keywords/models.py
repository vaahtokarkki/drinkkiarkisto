from application import db
from application.models import Base

class Keyword(Base):
    __tablename__ = "keyword"
    
    name = db.Column(db.String(144), nullable=False)
    accepted = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        self.accepted = False