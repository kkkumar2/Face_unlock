from pydantic import BaseModel

class Face_verification(BaseModel):
    mode: str
    # image_area: str