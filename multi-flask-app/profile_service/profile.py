# profile_service/app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    return jsonify({
        "username": username,
        "bio": f"This is {username}'s profile.",
        "interests": ["docker", "flask", "ci/cd"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
