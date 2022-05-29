
from pymongo import MongoClient
import pymongo


try:
    # client = MongoClient("mongodb://sandeepjena:Siku8339@cluster0-shard-00-00.tetcj.mongodb.net:27017,cluster0-shard-00-01.tetcj.mongodb.net:27017,cluster0-shard-00-02.tetcj.mongodb.net:27017/?ssl=true&replicaSet=atlas-tzvisj-shard-0&authSource=admin&retryWrites=true&w=majority")
    
    # client = pymongo.MongoClient("mongodb+srv://mksaquib:mksaquib@cluster0.tetcj.mongodb.net/?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

    client = MongoClient("localhost",27017)

except pymongo.errors.ConfigurationError as e :
    raise e
except pymongo.errors.ConnectionFailure as f:
    raise f
    
store = client.storehash
db = store['All_User_Data']