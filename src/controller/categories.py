from flask import Blueprint, jsonify, request
from src.service.categories import category_service
from flask import make_response


category_bp = Blueprint('category_bp', __name__, url_prefix='/category')

service = category_service()


@category_bp.route('/', methods=['GET'])
def get_all_users():
    user_id = request.args.get('user_id')
    data, status_code = service.get_all(user_id)
    response = make_response(data, status_code)
    return response, status_code


@category_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    user, status_code = service.create(data)
    return user, status_code


@category_bp.route('/<int:id>', methods=['GET'])
def get_id(id):
    data, status_code = service.get_by_id(id)
    response = make_response(data, status_code)
    return response, status_code


@category_bp.route('/<int:id>', methods=['PUT'])
def edit_category(id):
    data = request.get_json()
    response = service.edit_category(id, data)
    return response


@category_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    response = service.delete_category(id)
    return response
