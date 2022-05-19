
from pymongo import MongoClient

client = MongoClient("mongodb+srv://prince:<password>@cluster0.xfinu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
store = client.storehash
db = store['All_User_Data']