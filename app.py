from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Selamat datang di API DevSecOps!"})

@app.route('/user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    conn = get_db_connection()
    # Contoh bad practice (SQL Injection) agar terdeteksi oleh SAST tool (Bandit)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    users = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in users])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)