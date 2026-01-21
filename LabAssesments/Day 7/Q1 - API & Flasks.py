from flask import Flask, jsonify, request
# 1.
app = Flask(__name__)

users = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Bharadwaj"}
]

#2
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200

    return jsonify({"error", "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error", "Name required"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True)