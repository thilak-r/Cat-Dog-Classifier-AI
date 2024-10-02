from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

try:
    model = load_model('animal_classifier_model.h5')
except Exception as e:
    raise RuntimeError("Error loading the model. Make sure the model file exists and is not corrupted.") from e

class_labels = ['cat', 'dog'] 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', error="No file part in the request."), 400

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error="No selected file."), 400

    # Ensure the file is an image
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return render_template('index.html', error="Invalid file type. Please upload an image (PNG, JPG, JPEG)."), 400

    try:
        img_path = os.path.join('static', file.filename)
        file.save(img_path)

        # Prepare the image for the model
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize the image

        # Make a prediction
        predictions = model.predict(img_array)
        predicted_class = class_labels[np.argmax(predictions)]

        return render_template('index.html', prediction=predicted_class, img_path=img_path)

    except Exception as e:
        return render_template('index.html', error="An error occurred during image processing."), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

