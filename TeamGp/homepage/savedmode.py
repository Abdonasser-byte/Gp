from keras.models import load_model
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from io import BytesIO
from keras.models import model_from_json

def preprocessing(image):
    
    ret = np.array(image)
    
    image1 = cv2.resize(ret, (256, 256))
    image2 = cv2.normalize(image1, None, 0, 1.0, cv2.NORM_MINMAX , dtype=cv2.CV_32F) 
    image1 = np.expand_dims(image2, 0)
    return image1


def postprocseesing (predicted_image):
    predicted_image = predicted_image > 0.5
    return predicted_image

def predict(image):
   
    model_path = "G:/DataSet/my_model_weights.h5"

    with open("G:/DataSet/my_model.json", "r") as json_file:
        loaded_model_json = json_file.read()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(model_path)

    ret = preprocessing(image)
    prediction = (loaded_model.predict(ret)[0,:,:,0] > 0.5).astype(np.uint8)
    result = postprocseesing(prediction)
    buffer = BytesIO()
    predicted_mask_image = Image.fromarray(result)
    predicted_mask_image.save(buffer, format='PNG')
    return predicted_mask_image

