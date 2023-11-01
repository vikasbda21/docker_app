from model import model_pipeline
from typing import Union
from fastapi import FastAPI, UploadFile
import io
from PIL import Image


app = FastAPI()


@app.get('/') 
def get_req():
    return {"method": "GET_Requiest"}


@app.post('/ask')
def ask(text: str, image: UploadFile):
    content = image.file.read()
    
    image = Image.open(io.BytesIO(content))
    #image = Image(image.file)

    result = model_pipeline(text, image)

    return {"answer": result}