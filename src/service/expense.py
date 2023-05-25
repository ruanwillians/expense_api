from src.repositories.expense import expenseRepository

repository = expenseRepository()


class expenseService():

    def get_all(self):
        data = repository.get_all()
        return data, 200

    def create(self, data):
        data = repository.create(data)
        return data, 201

    def edit_expense(self, id, data):
        data = repository.edit_expense(id, data)
        return data, 200
