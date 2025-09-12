import cv2
import mediapipe as mp
import webbrowser
import time
from collections import deque

# Initialize MediaPipe Hands and Drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Gesture recognition delay in seconds
GESTURE_DELAY = 3
last_gesture_time = time.time()
last_gesture = None

# Keep a rolling buffer of detected gestures
gesture_buffer = deque(maxlen=15)  # Check for consistency over last 15 frames

def recognize_gesture(hand_landmarks):
    finger_states = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        finger_states.append(1)
    else:
        finger_states.append(0)

    # Other fingers
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    for tip, pip in zip(tips, pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            finger_states.append(1)
        else:
            finger_states.append(0)

    if finger_states == [0, 0, 0, 0, 0]:
        return "fist"
    elif finger_states == [1, 0, 0, 0, 0]:
        return "thumbs_up"
    elif finger_states == [0, 1, 1, 0, 0]:
        return "peace"
    elif finger_states == [1, 1, 1, 1, 1]:
        return "open"
    else:
        return None

def open_link_for_gesture(gesture):
    gesture_map = {
        "fist": "https://google.com",
        "thumbs_up": "https://youtube.com",
        "peace": "https://github.com",
        "open": "https://wikipedia.org"
    }
    url = gesture_map.get(gesture)
    if url:
        print(f"Detected gesture: {gesture} → Opening: {url}")
        webbrowser.open(url)

def main():
    global last_gesture_time, last_gesture

    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(min_detection_confidence=0.75, min_tracking_confidence=0.75) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            gesture = None
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    gesture = recognize_gesture(hand_landmarks)
                    if gesture:
                        gesture_buffer.append(gesture)

                        # Check if the same gesture is detected consistently
                        if gesture_buffer.count(gesture) > 10:
                            current_time = time.time()
                            if gesture != last_gesture or (current_time - last_gesture_time) > GESTURE_DELAY:
                                open_link_for_gesture(gesture)
                                last_gesture = gesture
                                last_gesture_time = current_time
                                gesture_buffer.clear()

                    # Show gesture label
                    if gesture:
                        cv2.putText(frame, f"Gesture: {gesture}", (10, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Gesture Recognition", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Gesture recognition started...")
    main()
