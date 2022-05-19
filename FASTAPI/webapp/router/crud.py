from fastapi import APIRouter,Request
from webapp.schema import User 
# from utils.database import db
from bson import ObjectId

db = ""

route = APIRouter(
    prefix="/crud",
    tags=["crud"]
)

# =============== Starting CRUD operations ===================

@route.get("/{unique_id}")
def find_user(unique_id,request: Request):
    query = {"unique_id": unique_id}
    hash_data = [data for data in db.find(query)]


@route.post("/")
def create_user(data:User,request:Request):
    db.insert_one(dict(data))

@route.put("/{id}")
def update_user(id,data:User,request:Request):
    db.find_one_and_update(
                            {"_id":ObjectId(id)},
                            {"$set":dict(data)})

@route.delete("/{id}")
def delete(id,request:Request):
    db.find_one_and_delete({"_id":ObjectId(id)})


