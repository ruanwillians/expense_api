from datetime import datetime
from database import db
from sqlalchemy import Column, Float, Integer, DateTime, ForeignKey
from model import categories


class Expense(db.Model):
    __tablename__ = 'expense'

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def json(self):
        return {
            'value': self.value,
            'date': self.date
        }
