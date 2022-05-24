from FACE_VERIFICATION.validation import Verify
from utils.encrypt import Encrypt
from utils.calling import caller
import pickle

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
            return response
        if mode == "train":
            response = obj1.generate_embeds(frame_count=2,WINDOW=data['image_area'])
            print(response)
            return response
        if mode == "predict":
            response = obj1.verify(frame_count=1,WINDOW=data['image_area'])
            print(response)
            return response

    def encrypt_controller(self,unique_id=None,data=None,mode=None,_id=None):
        
<<<<<<< HEAD
        data1 = {"data":obj2.encrypt_data(unique_id,data)}
        ### test
        print(data1)
        with open("usedata.pkl",'wb') as f:
            pickle.dump(data1,f)
        ### test 

        # data2 = {"data":obj2.decrypt_data(unique_id,data1)} ## for testing purpose
        # print(data2)
        # return obj3.database_controller(unique_id,data1,mode=mode)
=======
        # data = {data:obj2.encrypt(unique_id,data)}
        return obj3.database_controller(unique_id,data,mode=mode,_id =_id)
>>>>>>> 10d6811458767000fadc5d84bccefff5882f2ec3
       

