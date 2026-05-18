# import necessary packages
import os
import cv2
import numpy as np
# import systemcheck
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

# initialize mediapipe by GOOGLE to detect location points of human hand
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model 
# model = load_model('mp_hand_gesture')
model = load_model('CNN.hdf5')
model.summary()

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)
face_detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Any one can be used 
Flag_to_GO = 1
Flag_to_STOP = 0

def control(frame):
    x, y, c = frame.shape

    frame = cv2.flip(frame, 1)
    
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    gray=cv2.cvtColor(framergb,cv2.COLOR_BGR2GRAY)
    
    faces=face_detector.detectMultiScale(gray,1.3,7)

    if not len(faces):
        cv2.putText(frame, "NO Detection", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)

######################################################################################################
        # No change in robot functionality
        Flag_to_GO = 1
        # Flag_to_STOP = 0
        cv2.imshow("ML OP", frame) 
        return Flag_to_GO
######################################################################################################

    else:
        faces = faces[0]
        left=faces[0]
        top=faces[1]
        width=faces[2]
        height=faces[3]
        cv2.rectangle(frame,(left,top),(left+width,top+height),color=(0,255,0))
            

        # Get hand landmark prediction
        result = hands.process(framergb)

        # print(result)
        
        className = ''

        # post process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # print(id, lm)
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                # Predict gesture
                prediction = model.predict([landmarks])
                # print(prediction)
                classID = np.argmax(prediction)
                className = classNames[classID]

                if className=="stop":
                    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)

######################################################################################################
                    # robot has to stop for 10-20 sec
                    Flag_to_GO = 0
                    # Flag_to_STOP = 1
                    cv2.imshow("ML OP", frame) 
                    return Flag_to_GO
######################################################################################################

                elif className=="peace":
                    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
######################################################################################################
                    # if condition satisfied robot can start again even before the 10-20 sec timer ends
                    # if timer is over then regardless it has to start automatically.
                    Flag_to_GO = 2
                    # Flag_to_STOP = 0
                    cv2.imshow("ML OP", frame) 
                    return Flag_to_GO
######################################################################################################
######################################################################################################
    # No change in robot functionality
    Flag_to_GO = 1
    # Flag_to_STOP = 0
    cv2.imshow("ML OP", frame) 
    return Flag_to_GO
######################################################################################################


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    flag = 0
    while True:
        _, frame = cap.read()

        Flag_to_GO= control(frame)

        # Show the final output
        # cv2.imshow("Output", frame) 

        if cv2.waitKey(1) == ord('q'):
            break

    # release the webcam and destroy all active windows
    cap.release()
    cv2.destroyAllWindows()
