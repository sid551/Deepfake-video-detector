# utils.py
import cv2
import numpy as np
from model.mesonet import Meso4

# Load the model
model = Meso4()
model.load('model/weights.h5')

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    predictions = []

    for _ in range(10):  # Process 10 frames
        ret, frame = cap.read()
        if not ret:
            break

        resized = cv2.resize(frame, (256, 256)) / 255.0
        input_data = np.expand_dims(resized, axis=0)
        prediction = model.predict(input_data)[0][0]
        predictions.append(prediction)

    cap.release()

    avg = np.mean(predictions)
    return "Deepfake Detected" if avg > 0.5 else "Real Video"
