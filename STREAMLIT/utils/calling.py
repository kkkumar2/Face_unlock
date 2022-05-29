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

    def database_controller(self,unique_id,data=None,mode=None,_id=None):
        
        URL = f"{self.BASE_URI}{self.END_POINT2}"
        if mode == 'Add':
            user = {"unique_id": unique_id,"data":data}
            json_data = json.dumps(user)
            response = requests.post(URL,data=json_data, headers=self.HEADERS, timeout=8000)
            print(response.status_code)
            if response.status_code == 201:
                return "Successfully Added"
            else:
                return "Error in Adding, please try again"
            
        elif mode == 'View':
            URL = f"{URL}/{unique_id}"
            response = requests.get(URL,timeout=8000)
            return json.loads(response.content)

        elif mode == 'Update':
            user = {"unique_id": unique_id,"data":data}
            json_data = json.dumps(user)
            URL = f"{URL}/{_id}"
            response = requests.put(URL, data=json_data,timeout=8000)
            if response.status_code == 201:
                return "Successfully updated"
            else:
                return "Error in update, please try again"

        elif mode == 'Delete':
            URL = f"{URL}/{_id}"
            response = requests.delete(URL, timeout=8000)
            if response.status_code == 301:
                return "Successfully Deleted"
            else:
                return "Error in delete, please try again"

