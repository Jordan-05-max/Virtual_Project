"""test classifier"""
import cv2
import pickle as pk
import numpy as np
import mediapipe as mp

model_dict = pk.load(open('./model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils
mp_drawings_style = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

labels_dict = {0: 'A', 1: 'B', 2: 'C'}
while True:
    data_aux = []
    x_ = []
    y_ = []
    ret, frame = cap.read()

    w, h, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawings.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawings_style.get_default_hand_landmarks_style(),
                mp_drawings_style.get_default_hand_connections_style())
        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                # data_aux.append(x)
                # data_aux.append(y)
                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        x1 = int(min(x_) * w) - 10
        y1 = int(min(y_) * h) - 10

        x2 = int(max(x_) * w) - 10
        y2 = int(max(y_) * h) - 10

        prediction = model.predict([np.asarray(data_aux)])
        predicted_char = labels_dict[int(prediction[0])]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame, predicted_char, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3,
                    (0, 0, 0), 3, cv2.LINE_AA)

    # print(predicted_char)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()