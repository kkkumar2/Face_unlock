from fastapi import APIRouter,Request,Response, status
from webapp.schema import User 
from webapp.database import db
from bson import ObjectId



route = APIRouter(
    prefix="/crud",
    tags=["crud"]
)

# =============== Starting CRUD operations ===================

@route.get("/{unique_id}")
def find_user(unique_id,request: Request,response: Response):
    query = {"unique_id": unique_id}
    hash_data = [data for data in db.find(query)]
    response.status_code = status.HTTP


@route.post("/")
def create_user(data:User,request:Request,response: Response):
    db.insert_one(dict(data))
    response.status_code = status.HTTP_201_CREATED
    

@route.put("/{unique_id}")
def update_user(unique_id,data:User,request:Request,response: Response):
    db.find_one_and_update(
                            {"_id":ObjectId(id)},
                            {"$set":dict(data)})
    response.status_code = status.HTTP_200_OK

@route.delete("/{unique_id}")
def delete(unique_id,request:Request,response: Response):
    db.find_one_and_delete({"_id":ObjectId(id)})
    response.status_code = status.HTTP_301_MOVED_PERMANENTLY

