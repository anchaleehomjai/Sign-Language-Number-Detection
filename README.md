# Sign-Language-Number-Detection

This project implements a **hand gesture recognition system** for detecting numbers **1-9** using a webcam. It utilizes **Computer Vision and Machine Learning** to detect and classify hand signs in real-time.

---

## 📌 Features
- 📷 **Real-time hand gesture detection** using OpenCV and MediaPipe
- 🔢 Recognizes **hand signs for numbers 1-9**
- 🏗 **Custom dataset collection tool** for training data
- 🎯 **Machine Learning model** based on **Random Forest Classifier**
- 📊 Performance evaluation with **accuracy metrics and confusion matrix visualization**

---

## 📂 Project Structure
```
.
├── README.md               # Project documentation
├── requirements.txt        # Dependencies
├── collect.py             # Script to collect images for training
├── dataset-creator.py     # Converts images into a dataset
├── model-trainer.py       # Trains the Machine Learning model
├── inference.py           # Runs real-time hand gesture detection
├── data/                  # Folder for collected image data
│   ├── 1/                 # Images for number 1
│   ├── 2/                 # Images for number 2
│   ├── ...
└── model.p                # Trained model (generated after training)
```

---

## 🚀 Installation
### 1️⃣ **Clone the repository**
```bash
git clone <repository-url>
cd Sign-Language-Number-Detection
```

### 2️⃣ **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 📝 Usage
### **1. Collect Training Data**
Run `collect.py` to capture hand gesture images:
```bash
python collect.py
```
- The script will create directories for each number (1-9)
- It will capture **100 images per number** using your webcam
- Press **'Q'** when ready to start capturing for each number

### **2. Process the Dataset**
Convert collected images into a dataset using:
```bash
python dataset-creator.py
```
- Extracts **hand landmarks** using MediaPipe
- Normalizes coordinates and saves them in `data.pickle`

### **3. Train the Model**
Train the machine learning model with:
```bash
python model-trainer.py
```
- Splits dataset into **training (80%)** and **testing (20%)**
- Trains a **Random Forest Classifier**
- Saves the trained model as `model.p`
- Displays **accuracy and confusion matrix**

### **4. Run Real-time Detection**
Use `inference.py` to detect hand signs in real time:
```bash
python inference.py
```
- Uses **webcam feed** to detect and classify numbers
- Draws **bounding boxes** and displays **predicted number**
- Press **'Q'** to exit

---

## 📊 Model Performance
- The model uses **Random Forest Classifier** for classification.
- The performance is evaluated using:
  - **Training Accuracy**
  - **Testing Accuracy**
  - **Confusion Matrix Visualization**

After training, a sample output might look like:
```
Training Accuracy: 98.5%
Testing Accuracy: 92.7%
```

---

## 🛠 Troubleshooting
| Issue                 | Solution |
|----------------------|----------|
| **Camera not working** | Ensure no other apps are using the webcam. Try changing `CAMERA_ID` in the script. |
| **Model not accurate** | Capture more images and retrain the model. Ensure lighting conditions are good. |
| **Missing model.p** | Run `model-trainer.py` to generate the model before running `inference.py`. |

---

## 🏗 Future Improvements
- Improve model accuracy using **Deep Learning (CNNs)**
- Add **hand gesture recognition for alphabets (A-Z)**
- Implement a **web-based interface** for real-time use

---

## 📜 Acknowledgment
This project is developed based on [sign-language-detector-python](https://github.com/computervisioneng/sign-language-detector-python) by [ComputerVisionEng](https://github.com/computervisioneng). The original project provided the foundation for hand gesture detection, and this version builds upon it with enhancements, modifications, and additional features.

The original repository is licensed under the **MIT License**, and we fully acknowledge and appreciate the work of the original authors. The license file from the original project has been retained to comply with its terms.

For more details, refer to the original repository: [GitHub - computervisioneng/sign-language-detector-python](https://github.com/computervisioneng/sign-language-detector-python).

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.



