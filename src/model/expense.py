from datetime import datetime
from database import db
from sqlalchemy import Column, Float, Integer, DateTime, ForeignKey, String
from src.model.categories import Categories


class Expense(db.Model):
    __tablename__ = 'expense'

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    description = Column(String)
    date = Column(String, nullable=False, default=datetime.now)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Categories', backref='expenses')

    def __init__(self, value, date, description, category_id):
        self.value = value
        self.date = date
        self.description = description
        self.category_id = category_id

    def json(self):
        return {
            "value": self.value,
            "date": self.date,
            "description": self.description
        }
