from flask import Blueprint, request, jsonify
import os
from services.yolo_service import YOLOService

predict_bp = Blueprint('predict', __name__)

UPLOAD_FOLDER = "static/uploads"
yolo = YOLOService("models/best_last.pt")


@predict_bp.route("/predict", methods=["POST"])
def predict():
    # ✅ Ambil file
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # ✅ Ambil species dari frontend
    species = request.form.get("species")

    if not species:
        return jsonify({"error": "Species is required (cat/dog)"}), 400

    # ✅ Simpan file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # 🔥 Kirim species ke YOLOService
    detections = yolo.predict(filepath, species)

    return jsonify({
        "status": "success",
        "species": species,
        "detections": detections
    })
