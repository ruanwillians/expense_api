from database import db
from sqlalchemy import Column, Float, Integer, String


class Categories(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(255), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def json(self):
        return {
            'name': self.name,
            'description': self.description
        }
