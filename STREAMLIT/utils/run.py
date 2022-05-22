from FACE_VERIFICATION.validation import Verify
from utils.encrypt import Encrypt
from utils.calling import caller

obj1 = Verify()
obj2 = Encrypt()
obj3 = caller()

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

    def encrypt_controller(self,data):
        mode = data['mode']
        if mode == "Add":
            encrypted_category = obj2.encrypt(data['category'])
            encrypted_username = obj2.encrypt(data['username'])
            encrypted_password = obj2.encrypt(data['password'])

        data = {"mode":mode, "encrypted_category":encrypted_category, 
        "encrypted_username":encrypted_username, "encrypted_password":encrypted_password}

        obj3.database_controller(data)

