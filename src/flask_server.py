from flask import Flask, jsonify, request
from users import add_user, list_users, user_exists, delete_user, update_user

app = Flask(__name__)


# TODO 
# ADD PUT ENDPOINT TO UPDATE USER
# ADD DELETE ENDPOINT TO DELETE USER






@app.route("/users/", methods=["GET"])
def get_users():
    users = list_users()
    return jsonify(users), 200

@app.route("/users/<name>", methods=["GET"])
def get_user(name):
    if user_exists(name):
        return jsonify({"exists": True, "user": name.strip()}), 200
    else:
        return jsonify({"exists": False, "error": "User not found"}), 404


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name", "") if data else ""
    success = add_user(name)
    if success:
        return jsonify({"message": "User created"}), 201
    else:
        return jsonify({"error": "invalid or duplicate user"}), 400



if __name__ == "__main__":
    app.run(debug=True)