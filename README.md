# Hand Gesture Recognition System

A real-time hand gesture recognition system built using **Python**, **OpenCV**, **MediaPipe**, and **TensorFlow/Keras**.  
This project detects hand gestures through a webcam and controls robot-like actions such as **GO**, **STOP**, and **RESUME** based on recognized gestures.

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

1. Webcam captures live video.
2. MediaPipe detects hand landmarks.
3. Landmarks are passed to the CNN model.
4. The model predicts the gesture.
5. Based on the gesture:
   - **stop** → Robot stops
   - **peace** → Robot resumes/start
6. Face detection ensures proper interaction handling.

The project uses:
- `Flag_to_GO = 0` → Stop
- `Flag_to_GO = 1` → Normal operation
- `Flag_to_GO = 2` → Resume/Start

---

## ✋ Supported Gestures

| Gesture | Action |
|---|---|
| stop | Stops the robot/system |
| peace | Resumes or starts the robot/system |

You can add more gestures by retraining the model.

---

## 📸 Demo Workflow

1. Run the application
2. Show your hand in front of the webcam
3. Perform a gesture:
   - ✋ Stop gesture → System stops
   - ✌️ Peace gesture → System resumes

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

- Add more gesture classes
- Improve model accuracy
- Integrate with IoT/robotics hardware
- Add GUI interface
- Use GPU acceleration
- Deploy as a web application
- Add voice feedback system

---

## 📌 Applications

- Robot control systems
- Smart home automation
- Touchless interfaces
- Sign language recognition
- Gaming controls
- Human-computer interaction
- Healthcare assistance systems

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---
