from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages', methods = ["GET", "POST"])
def messages():
    if request.method == "GET":
        messages = Message.query.order_by(Message.created_at).all()
        response = [message.to_dict() for message in messages]
        return make_response(jsonify(response), 200)
    elif request.method == "POST":
        data = request.get_json()
        new_user_info = Message(
            username = data.get("username"),
            body = data.get("body")
        )
        db.session.add(new_user_info)
        db.session.commit()

        return make_response(new_user_info.to_dict(), 201)
        



@app.route('/messages/<int:id>', methods = ["PATCH", "DELETE"])
def messages_by_id(id):
    message = Message.query.filter_by(id=id).first()
    if not message:
        return make_response(jsonify({"message":"Message does not exist"},404))
    
    if request.method == "PATCH":
        data = request.get_json()
        message.body= data.get("body", message.body)
        db.session.commit()
        return make_response(message.to_dict(), 200)
    
    if request.method == "DELETE":
        db.session.delete(message)
        return make_response({}, 204)

    

if __name__ == '__main__':
    app.run(port=5555)
