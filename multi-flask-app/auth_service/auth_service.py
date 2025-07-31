# auth_service/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    return jsonify({"message": f"User {data.get('username')} registered"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data.get("username") == "admin" and data.get("password") == "admin":
        return jsonify({"token": "mocked_jwt_token"}), 200
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
