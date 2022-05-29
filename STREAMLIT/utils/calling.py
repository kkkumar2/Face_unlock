import json
import requests
from dotenv import load_dotenv
import os

class caller:
    def __init__(self):
        # load_dotenv()
        # self.BASE_URI = os.getenv("BASE_URI")
        # self.HEADERS = {"Content-type": os.getenv("Content-type"),"accept": os.getenv("accept")}
        # self.END_POINT1 = os.getenv("END_POINT1")
        # self.END_POINT2 = os.getenv("END_POINT2")
        pass

    def database_controller(self,unique_id,data=None,mode=None,_id=None):
        
        URL = "http://127.0.0.1:8000/crud"
        # URL = "http://fastapi:8000/curd" used for docker compose
        if mode == 'Add':
            user = {"unique_id": unique_id,"data":data}
            json_data = json.dumps(user)
            response = requests.post(URL,data=json_data, headers=self.HEADERS, timeout=8000)
            # response = requests.post(URL,data=user, timeout=8000)
            print(response.status_code)
            return response
        elif mode == 'View':
            # user = {"unique_id":unique_id}
            # json_data = json.dump(user)
            URL = f"{URL}/{unique_id}"
            response = requests.get(URL,timeout=8000)
            return json.loads(response.content)

        elif mode == 'Update':
            user = {"unique_id": unique_id,"data":data}
            json_data = json.dumps(user)
            URL = f"{URL}/{_id}"
            response = requests.put(URL, data=json_data,timeout=8000)

        elif mode == 'Delect':
            URL = f"{URL}/{_id}"
            response = requests.delete(URL, timeout=8000)

