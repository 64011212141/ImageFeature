from fastapi import FastAPI
import pickle
import  base64
import numpy as np
import cv2
from app.code import gethog
from fastapi import FastAPI,HTTPException,Request
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

def Readb64(url):
    encodded_data = url.split(',',1)
    img_str = encodded_data[1]
    decode = base64.b64decode(img_str)
    img = cv2.imdecode(np.frombuffer(decode,np.uint8),cv2.IMREAD_GRAYSCALE)
    return img

@app.get("/")
def read_root():
    return {"messge " : "Hello,FastAPI"}

@app.get("/api/gethog")
async def read_str(data : Request):
    json = await data.json()
    item_str = json["img"]
    img =Readb64(item_str)
    hog = gethog(img)
    return {"message" : hog}