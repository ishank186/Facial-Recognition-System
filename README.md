# Face Recognition Attendance System

## Overview
The **Face Recognition Attendance System** is a Python-based project designed to recognize faces and log attendance. This project utilizes machine learning and computer vision techniques for face detection and recognition. The system captures live video input from a webcam, detects faces in real-time, and recognizes registered users.

## 🛠️ Tech Stack
- **Programming Language**: Python
- **Libraries Used**:
  - OpenCV: For face detection and image processing.
  - NumPy: For matrix operations.
  - Scikit-learn: For the KNN algorithm.
  - CSV: For attendance logging.
  - PyWin32: For text-to-speech functionality.

## ⚙️ Features
- Real-time face detection using OpenCV.
- Face recognition using the K-Nearest Neighbors (KNN) algorithm.
- User-friendly interface for collecting face data.
- Attendance logging in CSV format.

## 📁 Folder Structure
```
face_recognition_attendance_system/
├── data/
│   ├── haarcascade_frontalface_default.xml
│   ├── names.pkl
│   └── faces_data.pkl
├── Attendance/
├── face.py
└── new_register.py
```
1. **`data/`**: Contains the Haarcascade XML file for face detection and pickle files for storing user data.
2. **`Attendance/`**: Stores daily attendance records in CSV format.
3. **`face.py`**: The main script for face recognition and attendance logging.
4. **`new_register.py`**: Script to register new users by capturing their face data.

## 🚀 Installation and Setup
### Prerequisites
- Python 3.8 or later installed on your system.
- A working webcam.

### Dependencies
Install the required Python libraries:
```bash
pip install opencv-python numpy scikit-learn pywin32
```

## 📝 Usage
### Step 1: Register a New User
Run the `new_register.py` script to register a new user:
```bash
python new_register.py
```
1. Enter the user's name when prompted.
2. The system will collect 100 face samples using the webcam.
3. The face data will be stored in `data/names.pkl` and `data/faces_data.pkl`.

### Step 2: Start Face Recognition
Run the `face.py` script to start face recognition:
```bash
python face.py
```
1. The system will detect and recognize faces in real-time.
2. Recognized faces are displayed on the video feed with their names.
3. Attendance is logged in the `Attendance/` folder as a CSV file.

### Exiting the Program
- Press **`q`** to exit the video feed.

## 🔍 How it Works
1. **Face Detection**:
   - Uses the Haarcascade classifier to detect faces in the video feed.
2. **Face Recognition**:
   - Captured faces are resized and flattened into feature vectors.
   - The K-Nearest Neighbors (KNN) algorithm is used for recognition.
3. **Attendance Logging**:
   - Recognized names and timestamps are logged into a CSV file named `Attendance_<date>.csv`.

## 📧 Contact
For any questions or suggestions, feel free to contact:
- **Name**: Ishank Khare
- **Email**: [your_email@example.com]
- **GitHub**: [Ishank Khare](https://github.com/ishank186)

