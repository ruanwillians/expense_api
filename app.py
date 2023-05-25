from database import create_app, db
from src.controller.expense import expense_bp


app = create_app()
app.register_blueprint(expense_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
