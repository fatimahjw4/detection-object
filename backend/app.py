from flask import Flask
from flask_cors import CORS
from routes.predict import predict_bp
import os

app = Flask(__name__)

# 🔥FIX CORS DI SINI
CORS(app, resources={r"/*": {"origins": "*"}})

# config folder upload
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.register_blueprint(predict_bp)

@app.route("/")
def health():
    return {"status": "API running 🚀"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
