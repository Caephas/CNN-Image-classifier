from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
import cv2
from PIL import Image
import io

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('models/image_classification.h5')

@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            img = Image.open(io.BytesIO(file.read()))
            img = img.resize((256, 256))
            img_array = np.array(img) / 255.0
            prediction = model.predict(img_array[np.newaxis, ...])
            result = 'Happy image' if prediction < 0.5 else 'Sad image'
            return result
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)