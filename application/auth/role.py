from application import db
from application.models import Base

class Role(Base):
    name = db.Column(db.String(100))
    displayName = db.Column(db.String(100))
    users = db.relationship("User", backref='role')