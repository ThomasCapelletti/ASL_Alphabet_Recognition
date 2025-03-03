import os
import sys
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt
print(os.getcwd())
# Define ASL Labels
labels = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'Del', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 
          11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'Space', 
          21: 'T', 22: 'U', 23: 'V', 24: 'W', 25: 'X', 26: 'Y', 27: 'Z'}

# Get the current working directory
current_directory = os.getcwd()


# Check if the folder exists
if not os.path.exists(current_directory):
    print(f'The folder "ASL_Recognition APP" is not in your working directory ({current_directory}).')
    print("Please move it there or change the directory.")
    sys.exit()

# Load the ASL model
model_path = os.path.join(current_directory, "asl_model_final.keras")
if not os.path.exists(model_path):
    print(f"Model file not found: {model_path}")
    sys.exit()

model = load_model(model_path)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

class ASLApp(QWidget):
    def __init__(self):
        super().__init__()

        # UI Layout
        self.setWindowTitle("ASL Sign Recognition")
        self.setGeometry(200, 200, 800, 600)
        
        self.video_label = QLabel(self)
        self.prediction_label = QLabel("Prediction: ", self)
        self.saved_text_label = QLabel("Writing: ", self)

        self.save_button = QPushButton("Write", self)
        self.clear_button = QPushButton("Clear", self)

        # Button Click Events
        self.save_button.clicked.connect(self.save_prediction)
        self.clear_button.clicked.connect(self.clear_text)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.prediction_label)
        layout.addWidget(self.saved_text_label)
        layout.addWidget(self.save_button)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

        # Webcam Capture
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        # Variables
        self.current_prediction = None
        self.saved_predictions = ""

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Extract landmarks (x, y)
                landmarks = [coord for landmark in hand_landmarks.landmark for coord in (landmark.x, landmark.y)]
                landmarks = np.array(landmarks).flatten()

                if landmarks.shape[0] == 42:
                    landmarks = (landmarks - np.min(landmarks)) / (np.max(landmarks) - np.min(landmarks))
                    img_input = np.expand_dims(landmarks, axis=0)

                    # Predict ASL Sign
                    prediction = model.predict(img_input)
                    class_id = np.argmax(prediction)
                    confidence = np.max(prediction)

                    if confidence > 0.5:
                        self.current_prediction = labels.get(class_id, "Unknown")
                    else:
                        self.current_prediction = "Low Confidence"

                    self.prediction_label.setText(f"Prediction: {self.current_prediction}")

        # Convert frame to QImage and show in UI
        h, w, ch = frame.shape
        qimg = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qimg))

    def save_prediction(self):
        if self.current_prediction:
            if self.current_prediction == "Del":
                self.saved_predictions = self.saved_predictions[:-1]
            elif self.current_prediction == "Space":
                self.saved_predictions += " "
            else:
                self.saved_predictions += self.current_prediction

            self.saved_text_label.setText(f"Writing: {self.saved_predictions}")

    def clear_text(self):
        self.saved_predictions = ""
        self.saved_text_label.setText("Writing: ")

    def closeEvent(self, event):
        self.cap.release()
        self.timer.stop()
        event.accept()

# Run the App
if __name__ == "__main__":
    app = QApplication([])
    window = ASLApp()
    window.show()
    app.exec_()
