# import cv2
# import pickle
# import numpy as np
# import os
# import csv
# import time
# from datetime import datetime
# import win32com.client
# from sklearn.neighbors import KNeighborsClassifier
# from win32com.client import Dispatch

# # Function to convert text to speech
# def speak(text):
#     speaker = Dispatch("SAPI.SpVoice")
#     speaker.Speak(text)

# # Function to log attendance
# def log_attendance(name, timestamp):
#     date = datetime.now().strftime("%d-%m-%Y")
#     attendance = [name, timestamp]
#     file_path = f"Attendance/Attendance_{date}.csv"

#     # Write attendance to CSV
#     with open(file_path, "a", newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         if csvfile.tell() == 0:  # Check if file is empty to write headers
#             writer.writerow(['NAME', 'TIME'])
#         writer.writerow(attendance)

# # Function to collect faces for a new user
# def collect_faces(name):
#     video = cv2.VideoCapture(0)
#     face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
    
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
#             faces_data.append(resized_img)

#             cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
#             cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

#         cv2.imshow("Collecting Faces", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     video.release()
#     cv2.destroyAllWindows()

#     faces_data = np.asarray(faces_data)
#     return faces_data.reshape(100, -1)  # Reshape for KNN input

# # Main routine
# # def main():
# #     # Initialize data paths
# #     names_path = 'data/names.pkl'
# #     faces_data_path = 'data/faces_data.pkl'

# #     # Check if names.pkl and faces_data.pkl exist
# #     if not os.path.isfile(names_path) or not os.path.isfile(faces_data_path):
# #         name = input("Enter Your Name: ")
# #         faces_data = collect_faces(name)

# #         # Save names and faces data
# #         names = [name] * 100

# #         with open(names_path, 'wb') as f:
# #             pickle.dump(names, f)

# #         with open(faces_data_path, 'wb') as f:
# #             pickle.dump(faces_data, f)

# #     # Load trained data
# #     with open(names_path, 'rb') as w:
# #         LABELS = pickle.load(w)
# #     with open(faces_data_path, 'rb') as f:
# #         FACES = pickle.load(f)

# #     print('Shape of Faces matrix --> ', FACES.shape)

# #     # Initialize KNN model
# #     knn = KNeighborsClassifier(n_neighbors=5)
# #     knn.fit(FACES, LABELS)

# #     # Set up video capture and face detection
# #     video = cv2.VideoCapture(0)
# #     face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# #     recognized_faces = set()  # To track already recognized faces and avoid duplicate entries

# #     print("Starting attendance detection. Press 'q' to exit.")
    
# #     while True:
# #         ret, frame = video.read()
# #         if not ret:
# #             print("Failed to grab frame.")
# #             break
            
# #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# #         for (x, y, w, h) in faces:
# #             crop_img = frame[y:y+h, x:x+w]
# #             resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
# #             output = knn.predict(resized_img)

# #             timestamp = datetime.now().strftime("%H:%M:%S")
# #             recognized_name = str(output[0])

# #             # Log attendance if the face is recognized and hasn't been logged already
# #             if recognized_name not in recognized_faces:
# #                 log_attendance(recognized_name, timestamp)
# #                 recognized_faces.add(recognized_name)  # Avoid duplicates

# #             # Draw the rectangle around the face and display the name
# #             cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
# #             cv2.putText(frame, recognized_name, (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

# #         cv2.imshow("Frame", frame)

# #         # Exit when 'q' is pressed
# #         if cv2.waitKey(1) & 0xFF == ord('q'):
# #             break

# #     video.release()
# #     cv2.destroyAllWindows()

# def main():
#     # Initialize data paths
#     names_path = 'data/names.pkl'
#     faces_data_path = 'data/faces_data.pkl'

#     # Check if names.pkl and faces_data.pkl exist
#     if not os.path.isfile(names_path) or not os.path.isfile(faces_data_path):
#         name = input("Enter Your Name: ")
#         faces_data = collect_faces(name)

#         # Save names and faces data
#         names = [name] * 100

#         with open(names_path, 'wb') as f:
#             pickle.dump(names, f)

#         with open(faces_data_path, 'wb') as f:
#             pickle.dump(faces_data, f)

#     # Load trained data
#     with open(names_path, 'rb') as w:
#         LABELS = pickle.load(w)
#     with open(faces_data_path, 'rb') as f:
#         FACES = pickle.load(f)

#     print('Shape of Faces matrix --> ', FACES.shape)

#     # Initialize KNN model
#     knn = KNeighborsClassifier(n_neighbors=5)
#     knn.fit(FACES, LABELS)

#     # Set up video capture and face detection
#     video = cv2.VideoCapture(0)
#     face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

#     recognized_faces = set()  # To track already recognized faces and avoid duplicate entries

#     print("Starting attendance detection. Press 'q' to exit.")
    
#     while True:
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
#             flattened_img = gray_img.flatten().reshape(1, -1)  # Reshape for KNN input
#             output = knn.predict(flattened_img)

#             timestamp = datetime.now().strftime("%H:%M:%S")
#             recognized_name = str(output[0])

#             # Log attendance if the face is recognized and hasn't been logged already
#             if recognized_name not in recognized_faces:
#                 log_attendance(recognized_name, timestamp)
#                 recognized_faces.add(recognized_name)  # Avoid duplicates

#             # Draw the rectangle around the face and display the name
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
#             cv2.putText(frame, recognized_name, (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

#         cv2.imshow("Frame", frame)

#         # Exit when 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     video.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()

import cv2
import pickle
import numpy as np
import os
import pymysql
import datetime
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier

# Connect to MySQL database
db = pymysql.connect(
    host="localhost",
    user="root",        # Your MySQL username
    password="",        # Your MySQL password
    database="face_recognition_attendance"
)

# Function to mark attendance in the MySQL database
def mark_attendance(name):
    cursor = db.cursor()
    date = datetime.date.today()
    time = datetime.datetime.now().time()

    # Insert attendance record into the database
    query = "INSERT INTO attendance (name, date, time) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, date, time))
    db.commit()
    cursor.close()
    print(f"Attendance marked for {name}")

# Function to collect faces for a new user
def collect_faces(name):
    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
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
            faces_data.append(resized_img)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
            cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

        cv2.imshow("Collecting Faces", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    faces_data = np.asarray(faces_data)
    return faces_data.reshape(100, -1)  # Reshape for KNN input

# Main function for face recognition and attendance logging
def main():
    # Initialize data paths
    names_path = 'data/names.pkl'
    faces_data_path = 'data/faces_data.pkl'

    # Check if names.pkl and faces_data.pkl exist
    if not os.path.isfile(names_path) or not os.path.isfile(faces_data_path):
        name = input("Enter Your Name: ")
        faces_data = collect_faces(name)

        # Save names and faces data
        names = [name] * 100

        with open(names_path, 'wb') as f:
            pickle.dump(names, f)

        with open(faces_data_path, 'wb') as f:
            pickle.dump(faces_data, f)

    # Load trained data
    with open(names_path, 'rb') as w:
        LABELS = pickle.load(w)
    with open(faces_data_path, 'rb') as f:
        FACES = pickle.load(f)

    print('Shape of Faces matrix --> ', FACES.shape)

    # Initialize KNN model
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(FACES, LABELS)

    # Set up video capture and face detection
    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    recognized_faces = set()  # To track already recognized faces and avoid duplicate entries

    print("Starting attendance detection. Press 'q' to exit.")

    while True:
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
            flattened_img = gray_img.flatten().reshape(1, -1)  # Reshape for KNN input
            output = knn.predict(flattened_img)

            timestamp = datetime.now().strftime("%H:%M:%S")
            recognized_name = str(output[0])

            # Log attendance if the face is recognized and hasn't been logged already
            if recognized_name not in recognized_faces:
                mark_attendance(recognized_name)  # Log attendance to the database
                recognized_faces.add(recognized_name)  # Avoid duplicates

            # Draw the rectangle around the face and display the name
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
            cv2.putText(frame, recognized_name, (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

        cv2.imshow("Frame", frame)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

