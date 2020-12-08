import uvicorn
from fastapi import FastAPI
from coronas import Corona
from flask import Flask, render_template, request
import numpy as np
import pickle

app = FastAPI()
model = pickle.load(open('modified_predict_proba_xgb_10.pkl','rb'))

# app = Flask(__name__)

@app.get('/')
def index():
    return {'message': 'Hello World'}
@app.get('/{name}')
def get_name(name:str):
    return {'message': f'Hello {name}'}

@app.post('/predict')
def predict(data:Corona):
    data = data.dict()
    age=data['age']
    temperature=data['temperature']
    pulse=data['pulse']
    rr=data['rr']
    rhonchi=data['rhonchi']
    wheezes=data['wheezes']
    cough=data['cough']
    fever=data['fever']
    loss_of_smell=data['loss_of_smell']
    loss_of_taste=data['loss_of_taste']
    listt = [[age, temperature, pulse, rr, rhonchi, wheezes, cough, fever, loss_of_smell, loss_of_taste]];
    prediction = model.predict_proba(np.array(listt, dtype='f'))[:,0]
    if(prediction[0]<0.5):
        prediction="negative"
    else:
        prediction="positive"
    return {'prediction': prediction}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)















