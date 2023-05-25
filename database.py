from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# conf de migração
migrate = Migrate()

db = SQLAlchemy()


def create_app():
    # Criar a instância do Flask
    app = Flask(__name__)

    # Define a URL do banco de dados com base nas variáveis de ambiente
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:BqKoZ2JgHBYtwXMVQyJn@containers-us-west-206.railway.app:5771/railway"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Registrar a extensão SQLAlchemy no aplicativo Flask
    migrate.init_app(app, db)  # Inicializar a extensão de migração

    return app
