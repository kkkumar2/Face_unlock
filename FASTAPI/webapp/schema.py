from pydantic import BaseModel


# def UserEntity(item) :
#     return {
#         "id":str(item['_id']),
#         "unique_id": item['unique_id'],
#         "hassing_value":item['hassing_value']
#     }

# def UsersEntity(entity) -> list:
#     return[UserEntity(item) for item in entity]

class User(BaseModel):
    unique_id:str 
    hassing_value:str

