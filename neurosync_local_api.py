# This software is licensed under a **dual-license model**
# For individuals and businesses earning **under $1M per year**, this software is licensed under the **MIT License**
# Businesses or organizations with **annual revenue of $1,000,000 or more** must obtain permission to use this software commercially.

from flask import request, jsonify
import numpy as np
import torch
import flask
import base64
import time

from utils.generate_face_shapes import generate_facial_data_from_bytes
from utils.model.model import load_model
from utils.config import config

app = flask.Flask(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Activated device:", device)

model_path = "utils/model/model.pth"
blendshape_model = load_model(model_path, config, device)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/audio_to_blendshapes", methods=["POST"])
def audio_to_blendshapes_route():
    start = time.perf_counter()
    if request.json:
        audio_bytes = request.json["audio"]
        audio_bytes = base64.b64decode(audio_bytes)
        print(f"Parsing took {time.perf_counter() - start:.4f} seconds")

        generated_facial_data = generate_facial_data_from_bytes(
            audio_bytes, blendshape_model, device, config
        )
        print(f"First step took {time.perf_counter() - start:.4f} seconds")
        generated_facial_data_list = (
            generated_facial_data.tolist()
            if isinstance(generated_facial_data, np.ndarray)
            else generated_facial_data
        )
        end = time.perf_counter()
        print(f"Total request took {end - start:.4f} seconds on device: {device}")

        return jsonify({"blendshapes": generated_facial_data_list})

    return jsonify({"error": "bad payload"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
