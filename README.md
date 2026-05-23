# Hand Gesture Recognition 

Sign Language Translation System for Deaf Communication ✋🧠

A real-time sign language translation system developed using **Python**, **OpenCV**, **MediaPipe**, and **TensorFlow/Keras** to help communicate with deaf and speech-impaired people through hand gesture recognition.

The system captures hand gestures through a webcam, detects sign language gestures using deep learning, and translates them into understandable actions or commands in real time.

The system also includes **face detection** for improved interaction logic and uses a trained CNN model for gesture classification.

---

## 🚀 Features

- Real-time webcam-based gesture recognition
- Hand landmark detection using MediaPipe
- Deep Learning gesture classification using CNN
- Face detection using Haar Cascade
- Supports gesture-based control logic
- Lightweight and fast execution
- Easy to customize with new gestures

---

## 🛠️ Technologies Used

- Python
- OpenCV
- TensorFlow / Keras
- MediaPipe
- NumPy

---

## 📂 Project Structure

```bash
Gesture_recog/
│
├── main.py                                 # Main application file
├── CNN.hdf5                                # Trained CNN model
├── gesture.names                           # Gesture labels
├── haarcascade_frontalface_default.xml     # Haar Cascade face detector
├── data.pickle                             # Dataset / processed data
├── systemcheck.pyc                         # Compiled system file
└── README.md                               # Project documentation
```

---

## ⚙️ How It Works

1. The webcam captures live video.
2. MediaPipe detects hand landmarks from the user's hand.
3. The extracted landmarks are passed to the trained CNN model.
4. The model predicts the corresponding sign language gesture.
5. The recognized gesture is translated into an action or communication output.
6. Face detection improves interaction reliability..


## ✋ Supported Gestures

| Gesture | Action |
|---|---|
| stop | Stops the robot/system |
| peace | Resumes or starts the robot/system |

You can add more gestures by retraining the model.

---


## ⚙️ How the System Works

1. The webcam captures live video input from the user.
2. MediaPipe detects hand landmarks from the captured hand gestures.
3. The extracted hand landmark coordinates are sent to the trained CNN model.
4. The deep learning model predicts the corresponding sign language gesture.
5. The recognized gesture is translated into meaningful communication output in real time.
6. Face detection is used to improve interaction accuracy and detection reliability.
7. The translated gesture helps bridge communication between deaf and non-sign language users.  

Press **Q** to exit.

---

## 🔧 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/gesture-recognition.git
cd gesture-recognition
```

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate environment:

#### Windows
```bash
venv\Scripts\activate
```

#### Linux/Mac
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Required Libraries

```bash
pip install opencv-python mediapipe tensorflow numpy
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🧠 Model Information

The project uses a trained CNN model:

```python
model = load_model('CNN.hdf5')
```

The model predicts gestures from hand landmark coordinates extracted using MediaPipe.

---

## 📷 Hand Landmark Detection

MediaPipe Hands is used to detect 21 hand landmarks in real time.

```python
mpHands = mp.solutions.hands
```

These landmarks are fed into the neural network for prediction.

---

## 👤 Face Detection

Face detection is implemented using Haar Cascade:

```python
face_detector=cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)
```

This ensures gesture processing occurs under valid conditions.

---

## 🧪 Future Improvements

- Add complete sign language sentence translation
- Convert gestures into speech output
- Support multiple languages
- Improve model accuracy
- Mobile application integration
- Real-time text generation
- Cloud deployment support

---

## 📌 Applications

- Deaf and mute communication systems
- Smart assistive technologies
- Human-computer interaction
- AI-based accessibility tools
- Educational support systems
- Healthcare communication assistance

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---
