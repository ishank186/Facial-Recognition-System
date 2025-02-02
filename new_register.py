# # 

# import cv2
# import pickle
# import numpy as np
# import os
# import csv
# from sklearn.neighbors import KNeighborsClassifier

# # Function to collect faces for a new user
# def collect_faces(name):
#     video = cv2.VideoCapture(0)
    
#     # Dynamically construct the Haarcascade file path
#     face_cascade_path = os.path.join('face_recognition_attendance_system', 'data', 'haarcascade_frontalface_default.xml')
#     face_cascade = cv2.CascadeClassifier(face_cascade_path)
    
#     # Debugging: Check if the Haarcascade file was loaded
#     print("Haarcascade file path:", face_cascade_path)
#     if face_cascade.empty():
#         print("Error: Haarcascade file could not be loaded. Check the path.")
#         return

#     faces_data = []

#     print(f"Collecting faces for {name}. Press 'q' to stop.")

#     while len(faces_data) < 100:
#         ret, frame = video.read()
#         if not ret:
#             print("Failed to grab frame.")
#             break
            
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             crop_img = frame[y:y+h, x:x+w]
#             resized_img = cv2.resize(crop_img, (50, 50))
#             gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
#             faces_data.append(gray_img)

#             cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
#             cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

#         cv2.imshow("Collecting Faces", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     video.release()
#     cv2.destroyAllWindows()

#     faces_data = np.asarray(faces_data)
#     return faces_data.reshape(100, -1)  # Reshape for KNN input (100 samples of 2500 features)

# # Function to register a new user
# def register_new_user():
#     name = input("Enter the new user's name: ")
#     faces_data = collect_faces(name)
#     if faces_data is None:
#         print("Failed to collect faces. Exiting.")
#         return
    
#     # Load existing names and faces data
#     if os.path.isfile('face_recognition_attendance_system/data/names.pkl') and os.path.isfile('face_recognition_attendance_system/data/faces_data.pkl'):
#         with open('face_recognition_attendance_system/data/names.pkl', 'rb') as f:
#             LABELS = pickle.load(f)
#         with open('face_recognition_attendance_system/data/faces_data.pkl', 'rb') as f:
#             FACES = pickle.load(f)
#     else:
#         LABELS = []
#         FACES = np.empty((0, 2500))  # Adjust size as needed

#     # Append new name and faces data
#     LABELS += [name] * 100
#     FACES = np.append(FACES, faces_data, axis=0)

#     # Save updated names and faces data
#     with open('face_recognition_attendance_system/data/names.pkl', 'wb') as f:
#         pickle.dump(LABELS, f)
#     with open('face_recognition_attendance_system/data/faces_data.pkl', 'wb') as f:
#         pickle.dump(FACES, f)

#     print(f"{name} has been registered successfully.")

# if __name__ == "__main__":
#     register_new_user()


import cv2
import pickle
import numpy as np
import os
import csv
from sklearn.neighbors import KNeighborsClassifier

# Function to collect faces for a new user
def collect_faces(name):
    video = cv2.VideoCapture(0)
    
    # Absolute path to Haarcascade file
    face_cascade_path = r"C:\Users\ASUS\Downloads\face_recognition_attendance_system\data\haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    
    # Debugging: Check if the Haarcascade file was loaded
    print("Using Haarcascade file at:", face_cascade_path)
    if face_cascade.empty():
        print("Error: Haarcascade file could not be loaded. Check the path.")
        return None

    faces_data = []

    print(f"Collecting faces for {name}. Press 'q' to stop.")

    while len(faces_data) < 100:
        ret, frame = video.read()
        if not ret:
            print("Failed to grab frame.")
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            crop_img = frame[y:y+h, x:x+w]
            resized_img = cv2.resize(crop_img, (50, 50))
            gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
            faces_data.append(gray_img)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
            cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

        cv2.imshow("Collecting Faces", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    faces_data = np.asarray(faces_data)
    return faces_data.reshape(100, -1)  # Reshape for KNN input (100 samples of 2500 features)

# Function to register a new user
def register_new_user():
    name = input("Enter the new user's name: ")
    faces_data = collect_faces(name)
    if faces_data is None:
        print("Failed to collect faces. Exiting.")
        return
    
    # Load existing names and faces data
    names_path = r"C:\Users\ASUS\Downloads\face_recognition_attendance_system\data\names.pkl"
    faces_data_path = r"C:\Users\ASUS\Downloads\face_recognition_attendance_system\data\faces_data.pkl"

    if os.path.isfile(names_path) and os.path.isfile(faces_data_path):
        with open(names_path, 'rb') as f:
            LABELS = pickle.load(f)
        with open(faces_data_path, 'rb') as f:
            FACES = pickle.load(f)
    else:
        LABELS = []
        FACES = np.empty((0, 2500))  # Adjust size as needed

    # Append new name and faces data
    LABELS += [name] * 100
    FACES = np.append(FACES, faces_data, axis=0)

    # Save updated names and faces data
    with open(names_path, 'wb') as f:
        pickle.dump(LABELS, f)
    with open(faces_data_path, 'wb') as f:
        pickle.dump(FACES, f)

    print(f"{name} has been registered successfully.")

if __name__ == "__main__":
    register_new_user()
