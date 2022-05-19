import cv2
from face_recognition.face_detector import FaceDetector
from face_recognition.feature_extract import FaceExtractor

obj1 = FaceDetector()
obj2 = FaceExtractor()

class Verify:
    def __init__(self):
        pass
    def validate(self,max_count):
        count = 0
        cap = cv2.VideoCapture(0)
        while True:
            _,frame = cap.read()
            image, boxes =  obj1.face_detector(frame)
            out = obj2.face_extractor(image, boxes)   
            count+=1    
            if count >= max_count:
                break