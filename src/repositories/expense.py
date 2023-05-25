from database import db
from src.model.expense import Expense
from database import db
from datetime import datetime
from uuid import uuid4


class expenseRepository():
    def save(self, data):
        db.session.add(data)
        db.session.commit()

    def generate_item(seld, data):
        description = data['description']
        date = data['date']
        value = data['value']
        category_id = data['category_id']

        item = Expense(date=date, description=description,
                       value=value, category_id=category_id)

        return item

    def get_all(self):
        data = Expense.query.all()
        return data

    def create(self, data):
        item = self.generate_item(data)
        self.save(item)
        return item

    def edit_expense(self, id, data):
        item = Expense.query.get(id)
        print(item)

        if not item:
            return None

        return item
