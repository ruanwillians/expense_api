from flask import jsonify
from database import create_app, db
from model import expense

app = create_app()


@app.route('/api', methods=['GET'])
def api():
    return jsonify("helloWord")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
