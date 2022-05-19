from fastapi import Request
from fastapi import APIRouter,Depends
from pydantic import BaseModel
from FASTAPI.webapp.schema import Face_verification
from face_recognition.validation import Verify

router = APIRouter(
    prefix="/Face_controller",
    tags=["Face_controller"]
)

obj1 = Verify()

@router.post("/")
def verify(data:Face_verification,request:Request):
    mode = data.mode
    print(mode)
    if mode == "verify":
        pass
    if mode == "train":
        pass
    if mode == "predict":
        pass

