# app.py
# Backend for your GlobalSave Bank HTML using Python Flask

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []

@app.route("/")
def home():
    return send_file("Spandex2.html")

# Create account
@app.route("/create-account", methods=["POST"])
def create_account():
    data = request.get_json()

    full_name = data.get("fullName")
    email = data.get("email")
    phone = data.get("phone")
    country = data.get("country")
    password = data.get("password")

    if not full_name or not email or not phone or not country or not password:
        return jsonify({
            "message": "All fields are required"
        }), 400

    new_user = {
        "id": len(users) + 1,
        "fullName": full_name,
        "email": email,
        "phone": phone,
        "country": country,
        "balance": 0
    }

    users.append(new_user)

    return jsonify({
        "message": "Account created successfully",
        "user": new_user
    })

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Run server
if __name__ == "__main__":
    app.run(debug=True)