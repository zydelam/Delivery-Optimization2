import numpy as np
import pickle
import joblib
import pandas as pd
from predictionlib import *
from flask import Flask, request
from flask import render_template

app=Flask(__name__)
model_name = 'rf_cv_trim_best.pkl'
pickle_in = open(model_name,"rb")
model = pickle.load(pickle_in)
kmeans_cust = pickle.load(open('kmeans_cust.pkl',"rb"))
kmeans_store = pickle.load(open('kmeans_store.pkl',"rb"))
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    print(final_features[0])
    d_date = prediction(model, kmeans_store, kmeans_cust, final_features[0])

    return render_template('index.html', prediction_text='Your order will be delivered on {}'.format(d_date))
    
    


if __name__=='__main__':
    app.run()