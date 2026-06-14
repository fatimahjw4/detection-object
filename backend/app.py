from flask import Flask
from flask_cors import CORS
from routes.predict import predict_bp
import os

app = Flask(__name__)

app.register_blueprint(predict_bp)

# 🔥FIX CORS DI SINI
CORS(app, resources={r"/*": {"origins": "*"}})

# config folder upload
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def health():
    return {"status": "API running 🚀"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
