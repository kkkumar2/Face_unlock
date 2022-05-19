import face_recognition
class FaceExtractor:
    def __init__(self):
        self.kEncodings = []

    def face_extractor(self, image, boxes):
        encodings = face_recognition.face_encodings(image, boxes)
        for encoding in encodings:
            self.kEncodings.append(encoding)
        return self.kEncodings
