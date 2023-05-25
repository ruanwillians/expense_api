from flask import Blueprint, jsonify, request
from src.service.expense import expenseService


expense_bp = Blueprint('expense_bp', __name__, url_prefix='/expenses')

service = expenseService()


@expense_bp.route('/', methods=['GET'])
def get_all_expenses():
    response = service.get_all()
    return response


@expense_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    service.create(data)
    return data


@expense_bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    data = request.get_json()
    response = service.edit_expense(id, data)
    return response
