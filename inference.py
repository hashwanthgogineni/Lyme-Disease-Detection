import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.image import array_to_img, img_to_array
classes = ["Lyme disease Undetected", "Lyme disease detected"]
model = load_model("model.h5")
def predict(img_path): 
 image = load_img(img_path, target_size=(128, 128))
 image = img_to_array(image)
 image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
 image = preprocess_input(image)
 yhat = model.predict(image)
 yhat = np.array(yhat)
 indices = np.argmax(yhat, axis=1)
 yhat = (yhat[0][indices])
 yhat = int(yhat*100)
 predicted_categories = [classes[i] for i in indices]
 output = predicted_categories[0]
 output = output + " with Confidence of "+ str(yhat) + '%'
 return output