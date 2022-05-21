import cv2
from FACE_VERIFICATION.face_detector import FaceDetector
from FACE_VERIFICATION.feature_extract import FaceExtractor
import os
import pandas as pd
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity




obj1 = FaceDetector()
obj2 = FaceExtractor()

class Verify:
    def __init__(self):
        self.metadata_dir = r"DATA\\Metadata"
        filename = "Embedding.pkl"
        self.embed_path = os.path.join(self.metadata_dir, filename)
        self.file_present = os.path.exists(self.embed_path)
        if self.file_present:
            self.embed = pd.read_pickle(self.embed_path)
        else:
            self.embed = {}

    def verify(self,frame_count,WINDOW):
        count = 0
        cap = cv2.VideoCapture(0)
        while True:
            _,frame = cap.read()
            image, boxes =  obj1.face_detector(frame,WINDOW)
            if boxes is None:
                continue
            current_embed = obj2.face_extractor(image, boxes)
            current_encodings = np.array(current_embed)
            if self.file_present:
                just_embed_keys = list(self.embed.keys())
                for ele in just_embed_keys:
                    full_encodings = np.array(self.embed[ele]) ## Full encodings for one person
                    score  = cosine_similarity(current_encodings, full_encodings)
                    if max(score[0]) * 100 > 90:
                        return {"msg":"Verified","unique_id":ele}
            else:
                return {"msg":"Not Verified"}
            count+=1    
            if count >= frame_count:
                break

    def generate_embeds(self,frame_count=10,WINDOW=None):
        count = 0
        final_current_embeddings = []
        cap = cv2.VideoCapture(0)
        while True:
            _,frame = cap.read()
            image, boxes =  obj1.face_detector(frame,WINDOW)
            current_embed = obj2.face_extractor(image, boxes)
            final_current_embeddings.append(current_embed)
            count+=1    
            if count >= frame_count:
                break
        if self.file_present:
            len_id = len(self.embed)
            unique_id = len_id
            self.embed[unique_id] = final_current_embeddings

        else:
            os.makedirs(self.metadata_dir,exist_ok=True)
            self.embed[0] = final_current_embeddings

        with open(self.embed_path, 'wb') as f:
                pickle.dump(self.embed, f)
        return "success"
           