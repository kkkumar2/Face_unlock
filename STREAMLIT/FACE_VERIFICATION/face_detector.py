import streamlit as st
import cv2 
import face_recognition
import os

##new

# from deepface import DeepFace
from fer import FER

##new

class FaceDetector:
    def __init__(self):
        # self.WINDOW = st.image([])
        pass

    def face_detector(self, img,WINDOW):
    
        RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(RGB, model='hog') 
        flag = False
        for (y1, x2, y2, x1) in boxes:
            # cropped_face = RGB[y1:y2, x1:x2]
            # analyze = DeepFace.analyze(img,actions=['emotions'])
            # emotion = analyze["dominanmt_emotion"]
            emo_detector = FER(mtcnn=True)
            captured_emotions = emo_detector.detect_emotions(RGB)
            dominant_emotion, emotion_score = emo_detector.top_emotion(RGB)

            flag = True
            cv2.rectangle(RGB, (x1, y1), (x2, y2), (255, 0, 0), 2)
            label_position = (x1-3,y1-3)
            cv2.putText(RGB,dominant_emotion,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            # face = cv2.resize(RGB, (200, 200))
            WINDOW.image(RGB)
        if flag:
            return RGB,boxes
        else:
            return None,None
