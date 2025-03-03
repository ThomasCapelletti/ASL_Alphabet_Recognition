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

```
ASL - Final Model  
├── ASL Application.py  (User interface for real-time recognition)  
├── alphabet tracking.ipynb  (Notebook for tracking analysis)  
├── asl_model_fine.keras  (Pre-trained final model)  

CNN - First Model  
├── Demo.ipynb (Initial CNN classification test using Kaggle dataset)  
├── asl-classification-using-cnn - V1.ipynb (Improved version with parameter tuning)  

CNN with Fixed Background  
├── asl_classification_our_hands.ipynb (Training on a custom dataset with a fixed background to reduce overfitting. This model was tested only on 5 letters to verify its effectiveness)  

Moving Around (CNN with Variable Background)  
├── testing while moving around.ipynb (Training with a dataset acquired while moving to improve generalization. This model was also initially tested only on 5 letters)  

Tracking Training (Hand Tracking + CNN)  
├── CNN tracking in training.ipynb (Experiment with CNN and selection of best images through hand tracking)  
├── tracking only weights.ipynb (Training based exclusively on hand coordinates instead of images)  

Useful Tools (Data Processing Scripts)  
├── data creator from video frames.py  (Extracting frames from videos)  
├── npy creator from folders.py  (Converting folders into .npy files)  
├── video flipper.py  (Flipping videos)  
├── video merger.py  (Merging videos)  

ASL - AI Report.pdf  (Complete project report)  

ASL Application.py (Also available in the repository's homepage for ease of use with any .keras file obtained from the tested models)  
```

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

## 💡 Acknowledgments  
- **Kaggle ASL Dataset**  
- **Google MediaPipe**  
- **TensorFlow/Keras Community**  

