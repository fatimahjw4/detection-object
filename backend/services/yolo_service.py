from ultralytics import YOLO
from utils.disease_mapping import map_disease_label


class YOLOService:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def predict(self, image_path, user_species):
        results = self.model(image_path)

        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                xyxy = box.xyxy[0].tolist()

                raw_label = self.model.names[cls_id]
                if raw_label == "hot-spot" and user_species == "cat":
                    continue
                
                # 🔥 Mapping di sini
                display_label = map_disease_label(raw_label, user_species)

                detections.append({
                    "raw_label": raw_label,
                    "display_label": display_label,
                    "confidence": round(conf, 3),
                    "bbox": {
                        "x1": int(xyxy[0]),
                        "y1": int(xyxy[1]),
                        "x2": int(xyxy[2]),
                        "y2": int(xyxy[3]),
                    }
                })

        return detections
