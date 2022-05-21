from FACE_VERIFICATION.validation import Verify

obj1 = Verify()

class RUN:
    def __init__(self):
        pass
    def controller(self,data):
        mode = data['mode']
        if mode == "verify":
            response = obj1.verify(frame_count=1,WINDOW=data['image_area'])
            print(response)
            return response['msg']
        if mode == "train":
            response = obj1.generate_embeds(frame_count=2,WINDOW=data['image_area'])
            print(response)
            return response
        if mode == "predict":
            response = obj1.verify(frame_count=1,WINDOW=data['image_area'])
            print(response)
            return response