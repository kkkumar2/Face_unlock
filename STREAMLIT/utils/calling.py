import json
import requests
from dotenv import load_dotenv
import os

class caller:
    def __init__(self):
        load_dotenv()
        self.BASE_URI = os.getenv("BASE_URI")
        self.HEADERS = {"Content-type": os.getenv("Content-type"),"accept": os.getenv("accept")}
        self.END_POINT1 = os.getenv("END_POINT1")
        self.END_POINT2 = os.getenv("END_POINT2")

    def database_controller(self,unique_id,data=None,mode=None):
        
        URL = f"{self.BASE_URI}{self.END_POINT2}"
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
            response = requests.get(URL,headers=self.HEADERS,timeout=8000)
            return json.loads(response.content)