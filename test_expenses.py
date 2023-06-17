import json
from app import app
import requests


def test_get_all_expenses():
    client = app.test_client()

    response = client.get('/expenses')

    assert response.status_code == 308


def test_get_all_categories():
    client = app.test_client()

    response = client.get('/category')

    assert response.status_code == 308


def test_get_all_user():
    client = app.test_client()

    response = client.get('/user')

    assert response.status_code == 308


def test_create_user():
    # Definir os dados a serem enviados no corpo da requisição
    data = {
        "name": "user",
        "email": "email@email.com",
        "password": "123456",
        "balance": 20.0
    }

    # Fazer a chamada POST para a rota /expenses
    response = requests.post('http://localhost:5000/user', json=data)

    # Verificar se o status code da resposta é 201 (Created)
    assert response.status_code == 201

    # Verificar se a resposta contém os dados inseridos
    expected_data = {
        "name": "user",
        "email": "user@email.com",
        "balance": 20.0
    }
    assert response.json() == expected_data


# def test_create_expense():
#     # Definir os dados a serem enviados no corpo da requisição
#     data = {
#         "date": "1683999687541",
#         "description": "teste",
#         "value": 20.0,
#         "category_id": 1
#     }

#     # Fazer a chamada POST para a rota /expenses
#     response = requests.post('http://localhost:5000/expenses', json=data)

#     # Verificar se o status code da resposta é 201 (Created)
#     assert response.status_code == 201

#     # Verificar se a resposta contém os dados inseridos
#     expected_data = {
#         "date": "1683999687541",
#         "description": "teste",
#         "value": 20.0,
#         "category_id": 1
#     }
#     assert response.json() == expected_data
