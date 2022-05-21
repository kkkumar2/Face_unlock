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

    def database_controller(self,data):
        print("data is",data)
        # json_data = json.dumps(data)
        URL = f"{self.BASE_URI}{self.END_POINT2}"
        # response = requests.post(URL,data=data, headers=self.HEADERS, timeout=8000)
        response = requests.post(URL,data=data, timeout=8000)
        print(response.status_code,response.content)
        return response.content