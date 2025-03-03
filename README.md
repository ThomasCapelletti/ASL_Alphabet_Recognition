# ASL Alphabet Recognition with AI

## 📌 Overview  
This project aims to recognize letters of the American Sign Language (ASL) alphabet using deep learning techniques. The system interprets ASL letters in real-time via webcam and converts them into text, enhancing communication accessibility. Several approaches have been tested, utilizing both Convolutional Neural Networks (CNN) and Multi-Layer Perceptrons (MLP), concluding that the optimal model is based on hand tracking with MediaPipe.  

## 🚀 Features  
- **Real-time ASL letter recognition** via webcam.  
- **Analysis of multiple models**, from traditional CNNs to an optimized MLP with MediaPipe.  
- **Use of public and custom-created datasets** to improve generalization.  
- **Final model based on 2D hand coordinates (X, Y) for faster and more efficient predictions.**  
- **SHAP interpretability analysis** to understand model decisions.  

## 📁 Repository Structure  
Since GitHub has storage limitations, only essential files have been uploaded. Datasets and large training files are not included, but each model can generate a `.keras` file that can be used with the ASL Application.py interface.  

🔹 ASL - Final Model
This folder contains the final and most effective model, which is already trained and ready for use:

ASL Application.py – The user interface for real-time ASL recognition.
alphabet tracking.ipynb – Jupyter notebook for tracking analysis and visualization.
asl_model_fine.keras – The pre-trained final model that achieves the best accuracy.
🔹 CNN - First Model
The first experimental CNN model trained on a public dataset:

Demo.ipynb – Initial CNN classification test using the Kaggle ASL dataset.
asl-classification-using-cnn - V1.ipynb – Improved version with parameter tuning.
🔹 CNN with Fixed Background
A model trained on a custom dataset with a fixed background to reduce overfitting:

asl_classification_our_hands.ipynb – This model was initially tested on only 5 letters to verify its effectiveness before full-scale training.
🔹 Moving Around (CNN with Variable Background)
A dataset was created while moving to test generalization capabilities:

testing while moving around.ipynb – Training with images captured in varying environments. Initially tested on 5 letters before full training.
🔹 Tracking Training (Hand Tracking + CNN)
Experiments integrating MediaPipe hand tracking into CNN models:

CNN tracking in training.ipynb – A CNN-based approach where only frames with clear hand visibility were selected.
tracking only weights.ipynb – A model trained exclusively on hand landmark coordinates instead of full images.
🔹 Useful Tools (Data Processing Scripts)
Scripts developed to assist with dataset creation and preprocessing:

data creator from video frames.py – Extracts frames from recorded videos to create datasets.
npy creator from folders.py – Converts folders of images into .npy files for efficient training.
video flipper.py – Flips videos horizontally to augment the dataset.
video merger.py – Merges multiple videos into a single file for dataset consistency.
🔹 Additional Files
ASL - AI Report.pdf – The complete project report detailing methodology, experiments, and results.
ASL Application.py – Also placed in the repository's root directory to facilitate usage with any .keras model obtained from the tested approaches.

## 🔧 Installation & Setup  
### 1️⃣ Clone the repository  
```bash  
git clone https://github.com/your_username/ASL-Alphabet-Recognition.git  
cd ASL-Alphabet-Recognition  
```

### 2️⃣ Install dependencies  
Make sure Python is installed, then run:  
```bash  
pip install -r requirements.txt  
```

### 3️⃣ Run the ASL Recognition Application  
```bash  
python ASL_Application.py  
```
This will launch the ASL recognition interface in real-time using the webcam.  

## 📊 Model Details  
Each tested model produced a `.keras` file that can be loaded and tested in the ASL Application.py interface. Additionally, `.npy` files for **x_train, x_test, y_train, y_test** can be saved for future use.  

### 1️⃣ CNN - First Model  
- **Based on a public dataset (Kaggle ASL Dataset)**  
- **Accuracy: 92.64%**, but suffered from overfitting  
- **Conclusion:** Effective recognition only for images similar to the training dataset  

### 2️⃣ CNN with Fixed Background  
- **Custom-created dataset** with a uniform background  
- **Accuracy: 98.64%**, but still had generalization issues  
- **Conclusion:** Not robust enough for external images  

### 3️⃣ CNN with Variable Background (Moving Around)  
- **Recorded videos with dynamic backgrounds** to improve generalization  
- **Reduced overfitting**, but accuracy dropped for unseen images  
- **Conclusion:** An improvement over previous models, but still not optimal  

### 4️⃣ Hand Tracking + CNN  
- **Used MediaPipe for hand tracking**  
- **Experimented with CNN and best frame selection**  
- **Conclusion:** Promising approach, but needed further optimization  

### 5️⃣ Final Model (MLP with MediaPipe)  
- **Best result: 99.74% accuracy**  
- **Uses only X and Y hand landmark coordinates, without images**  
- **Fast and lightweight, ideal for real-time applications**  
- **Conclusion:** The best approach among those tested, avoiding CNN overfitting issues  

## ❓ Why Are Datasets Not Included?  
I chose not to upload datasets for several reasons:  
1. **GitHub storage limitations**: The datasets contain thousands of images and videos, making them too large.  
2. **Privacy**: The recorded dataset videos contain personal images that cannot be shared publicly.  
3. **Encouraging the use of custom datasets**: Users can experiment by creating their own datasets or using publicly available ones.  
4. **Availability of pre-trained models**: I chose to upload only the `asl_model_fine.keras` file because it is the most functional and valid among those tested.  

## 📝 Possible Improvements  
- **Expand recognition beyond the ASL alphabet to include full words.**  
- **Enhance tracking robustness under varying lighting conditions.**  
- **Optimize the model for mobile and web applications.**  

