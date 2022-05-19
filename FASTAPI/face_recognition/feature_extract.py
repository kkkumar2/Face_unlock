import os
import face_recognition
import pickle
class FaceExtractor:
    def __init__(self):
        self.kEncodings = []
        self.kNames = []

    def face_extractor(self, rgb, boxes,text_input, type='train'):
        encodings = face_recognition.face_encodings(rgb, boxes)
        for encoding in encodings:
            self.kEncodings.append(encoding)
            self.kNames.append(text_input)
        if type == 'train':
            metadata_path = os.path.join(os.getcwd(),os.path.join('Data','metadata'))
            os.makedirs(metadata_path,exist_ok=True)
            embed_path = os.path.join(metadata_path,'Embeddings.pkl')
            classname_path = os.path.join(metadata_path,'classname.pkl')
            ## how to add unique key and dump in pickle.
            with open(embed_path, 'wb') as f:
                pickle.dump(self.kEncodings, f)
            with open(classname_path, 'wb') as f:
                pickle.dump(self.kNames, f)
        else:
            return encodings