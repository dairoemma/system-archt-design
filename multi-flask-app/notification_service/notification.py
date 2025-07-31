# notification_service/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    return jsonify({
        "status": "sent",
        "recipient": data.get("user"),
        "message": data.get("message")
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
