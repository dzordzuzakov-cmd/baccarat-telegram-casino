from flask import Flask, jsonify, send_from_directory
from database import get_balance

app = Flask(__name__)

@app.route('/api/balance/<int:user_id>')
def balance(user_id):
    bal = get_balance(user_id)
    return jsonify({"balance": bal})

@app.route('/webapp')
def webapp():
    return send_from_directory('webapp', 'index.html')

@app.route('/webapp/<path:path>')
def static_files(path):
    return send_from_directory('webapp', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
