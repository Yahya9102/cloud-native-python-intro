from flask import Flask, jsonify, request
from database import Base
from database import engine
from database import SessionLocal
from service.user_service import UserService
from models.user import User


app = Flask(__name__)

Base.metadata.create_all(engine)



@app.route("/users/", methods=["GET"])
def get_users():
    session = SessionLocal()
    service = UserService(session)

    try:
        users = service.list_users()
        result = []

        for user in users:
            result.append({"id": user.id, "name": user.name})

        return jsonify(result)
    finally:
        session.close()



#@app.route("/users/<name>", methods=["GET"])
#def get_user(name):
#   if user_exists(name):
#        return jsonify({"exists": True, "user": name.strip()}), 200
#    else:
#        return jsonify({"exists": False, "error": "User not found"}), 404


@app.route("/users", methods=["POST"])
def create_user():
    session = SessionLocal()
    service = UserService(session)

    try:
        data = request.get_json()
        name = data.get("name", "") if data else ""
        success = service.add_user(name)
        if success:
            return jsonify({"message": "User created"}), 201
        else:
            return jsonify({"error": "invalid or duplicate user"}), 400
    finally:
        session.close()




@app.route("/users", methods=["PUT"])
def update_user():
    session = SessionLocal()
    service = UserService(session)

    try:
        data = request.get_json()
        old_name = data.get("old_name", "") if data else ""
        new_name = data.get("new_name", "") if data else ""

        
        success, result = service.update_user(old_name,new_name)
        if success:
            return jsonify({"id": result.id, "name": result.name}), 201
        else:
            return jsonify({"error": result}), 400
    finally:
        session.close()




@app.route("/users", methods=["DELETE"])
def delete_user():
    session = SessionLocal()
    service = UserService(session)

    try:
        data = request.get_json()
        name = data.get("name", "") if data else ""
        success = service.delete_user(name)
        if success:
            return jsonify({"message": "User deleted"}), 201
        else:
            return jsonify({"error": "user not found"}), 400
    finally:
        session.close()



if __name__ == "__main__":
    app.run(debug=True)