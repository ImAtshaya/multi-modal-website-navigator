import cv2
import dlib
import webbrowser
import time
import numpy as np
from imutils import face_utils

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

URLS = {
    "smile": "https://youtube.com",
    "open_mouth": "https://instagram.com"
}

last_trigger_time = 0
TRIGGER_DELAY = 4  # seconds cooldown
gesture_start_time = 0
gesture_in_progress = None

# Adjusted thresholds
SMILE_MOUTH_RATIO_MAX = 0.42
SMILE_LIP_DISTANCE_MIN = 9

OPEN_MOUTH_LIP_DISTANCE_MIN = 25
OPEN_MOUTH_MOUTH_RATIO_MIN = 0.55

SMILE_HOLD_TIME = 0.5
OPEN_MOUTH_HOLD_TIME = 0.3

def main():
    global last_trigger_time, gesture_start_time, gesture_in_progress

    cap = cv2.VideoCapture(0)
    print("Starting webcam... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        if len(faces) == 0:
            gesture_start_time = 0
            gesture_in_progress = None
            last_trigger_time = 0
            cv2.imshow("Facial Gesture Recognition", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue

        for face in faces:
            shape = predictor(gray, face)
            shape_np = face_utils.shape_to_np(shape)
            mouth = shape_np[48:68]

            mouth_height = np.linalg.norm(mouth[14] - mouth[18])
            mouth_width = np.linalg.norm(mouth[12] - mouth[16])
            mouth_ratio = mouth_height / mouth_width
            top_lip = mouth[13]
            bottom_lip = mouth[19]
            lip_distance = np.linalg.norm(top_lip - bottom_lip)

            current_time = time.time()

            # Updated logic
            is_open_mouth = (lip_distance > OPEN_MOUTH_LIP_DISTANCE_MIN and mouth_ratio > OPEN_MOUTH_MOUTH_RATIO_MIN)
            is_smile = (mouth_ratio < SMILE_MOUTH_RATIO_MAX and 
                        lip_distance > SMILE_LIP_DISTANCE_MIN and 
                        not is_open_mouth)  # Don't allow smile if open mouth is true

            if current_time - last_trigger_time > TRIGGER_DELAY:
                if is_open_mouth:
                    if gesture_in_progress != "open_mouth":
                        gesture_in_progress = "open_mouth"
                        gesture_start_time = current_time
                    elif current_time - gesture_start_time >= OPEN_MOUTH_HOLD_TIME:
                        print("Open mouth detected! Opening Instagram.")
                        webbrowser.open(URLS["open_mouth"])
                        last_trigger_time = current_time
                        gesture_in_progress = None
                        gesture_start_time = 0

                elif is_smile:
                    if gesture_in_progress != "smile":
                        gesture_in_progress = "smile"
                        gesture_start_time = current_time
                    elif current_time - gesture_start_time >= SMILE_HOLD_TIME:
                        print("Smile detected! Opening YouTube.")
                        webbrowser.open(URLS["smile"])
                        last_trigger_time = current_time
                        gesture_in_progress = None
                        gesture_start_time = 0
                else:
                    gesture_in_progress = None
                    gesture_start_time = 0

            # Show landmarks (optional)
            for (x, y) in mouth:
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # Debug info
            cv2.putText(frame, f"lip_distance: {lip_distance:.1f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(frame, f"mouth_ratio: {mouth_ratio:.2f}", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("Facial Gesture Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
