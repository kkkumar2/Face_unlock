from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
import uvicorn
from webapp.router import crud,Face_Controller
import os



app  = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"], 
    allow_headers=["*"],
    max_age=2 
    )

app.include_router(crud.route)
app.include_router(Face_Controller.router)



if __name__ == '__main__':
    uvicorn.run(app)