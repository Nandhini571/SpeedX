from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # Use PostgreSQL in production
app.config["JWT_SECRET_KEY"] = "your_secret_key"

db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return render_template('index.html')
    

if __name__ == "__main__":
    socketio.run(app, debug=True)
