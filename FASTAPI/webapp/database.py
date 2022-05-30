
from pymongo import MongoClient
import pymongo


try:
    client = MongoClient("mongodb://sandeepjena:Siku8339@cluster0-shard-00-00.tetcj.mongodb.net:27017,cluster0-shard-00-01.tetcj.mongodb.net:27017,cluster0-shard-00-02.tetcj.mongodb.net:27017/?ssl=true&replicaSet=atlas-tzvisj-shard-0&authSource=admin&retryWrites=true&w=majority")
    
    # client = pymongo.MongoClient("mongodb+srv://mohan:faceunlock@faceunlock.jb92s.mongodb.net/?retryWrites=true&w=majority")

    client = MongoClient("localhost",27017)

except pymongo.errors.ConfigurationError as e :
    raise e
except pymongo.errors.ConnectionFailure as f:
    raise f
    
store = client.storehash
db = store['All_User_Data']