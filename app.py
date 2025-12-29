import os
import numpy as np
from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import keras

# ---- LOAD MODEL (SavedModel via TFSMLayer) ----
MODEL_PATH = "food11_best"

base = keras.layers.TFSMLayer(MODEL_PATH, call_endpoint="serving_default")

inputs = keras.Input(shape=(224, 224, 3), dtype="float32")
outputs = base(inputs)
model = keras.Model(inputs, outputs)

# ---- CLASS NAMES ----
CLASS_NAMES = [
    "apple_pie","cheesecake","chicken_curry","french_fries","fried_rice",
    "hamburger","hot_dog","ice_cream","omelette","pizza","sushi"
]

app = Flask(__name__)

# ---- IMAGE PREPROCESS ----
def prepare_image(file):
    img = load_img(file, target_size=(224, 224))
    arr = img_to_array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)
    return arr


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    uploaded_img = None

    if request.method == "POST":
        if "image" not in request.files:
            return render_template("index.html", prediction="No file uploaded")

        file = request.files["image"]

        if file.filename == "":
            return render_template("index.html", prediction="No file selected")

        # Save uploaded image
        os.makedirs("static", exist_ok=True)
        img_path = os.path.join("static", file.filename)
        file.save(img_path)

        img = prepare_image(img_path)

        # ---- PREDICT ----
        pred = model.predict(img)

        # TFSMLayer outputs dict sometimes
        if isinstance(pred, dict):
            pred = list(pred.values())[0]

        pred_idx = np.argmax(pred, axis=1)[0]
        prediction = CLASS_NAMES[pred_idx]
        uploaded_img = img_path

    return render_template("index.html", prediction=prediction, image_path=uploaded_img)


if __name__ == "__main__":
    app.run(host="0.0.0.0",
    port=int(os.environ.get("PORT", 8080)),
    debug=False)
