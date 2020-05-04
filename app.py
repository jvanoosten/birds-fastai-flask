#Importing necessary packages
import numpy as np
from flask import Flask, request, render_template
import pickle
from fastai.tabular import *
from fastai.vision import open_image
# import fastai
import os

#Saving the working directory and model directory
cwd = os.getcwd()
path = cwd + '/models'

#Initializing the FLASK API
app = Flask(__name__)

#Loading the saved model using fastai's load_learner method
model = load_learner(path, 'birds.pkl')

#Defining the home page for the web service
@app.route('/')
def home():
    return render_template('index.html')

#Writing api for inference using the loaded model
@app.route('/predict',methods=['POST'])
#Defining the predict method get input from the html page and to predict using the trained model
def predict():
    try:
        file = request.files['image']
        img = open_image(file)
        birdclass,underdata,probability = model.predict(img)
        return render_template('index.html', prediction_text='Bird prediction: {}, probablility : {} '.format(birdclass,probability))
    except:
        return render_template('index.html', prediction_text='Prediction Err !!!')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8080, debug=True)
