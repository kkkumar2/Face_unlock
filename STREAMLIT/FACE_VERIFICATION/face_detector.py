import streamlit as st
import cv2 
import face_recognition
import os
class FaceDetector:
    def __init__(self):
        # self.WINDOW = st.image([])
        pass

    def face_detector(self, img,WINDOW):
    
        RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(RGB, model='hog') 
        
        for (y1, x2, y2, x1) in boxes:
            cropped_face = RGB[y1:y2, x1:x2]
            cv2.rectangle(RGB, (x1, y1), (x2, y2), (255, 0, 0), 2)
            face = cv2.resize(cropped_face, (200, 200))
            WINDOW.image(RGB)
        if face is not None: 
            return face,boxes