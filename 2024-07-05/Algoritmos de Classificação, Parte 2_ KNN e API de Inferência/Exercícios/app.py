import numpy as np
from PIL import Image
import cv2
import joblib
from fastapi import FastAPI, UploadFile, File, Depends

app = FastAPI(docs_url='/', title='VC MASTER - PUC Rio')

pipeline = joblib.load('pipeline.pkl')


def apply_clahe(_image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    image_clahe = clahe.apply(_image)
    return image_clahe


def normalize_data(_image):
    return _image.astype('float32') / 255.0


def flatten_data(_image):
    return _image.flatten().reshape(1, -1)


@app.post('/predict')
async def predict(file: UploadFile = File(...)):

    image = Image.open(file.file)
    image_array = np.array(image)
    image = apply_clahe(image_array)
    image = normalize_data(image)
    image = flatten_data(image)
    prediction = pipeline.predict(image)

    return {"Prediction":  prediction[0]}
