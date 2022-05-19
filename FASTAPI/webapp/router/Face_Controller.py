from fastapi import Request
from fastapi import APIRouter,Depends
from pydantic import BaseModel
from webapp.schema import Face_verification
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
        response = obj1.validate(frame_count=1)
        return response
    if mode == "train":
        response = obj1.generate_embeds(frame_count=10)
        return response
    if mode == "predict":
        response = obj1.validate(frame_count=1)
        return response

