from flask import Flask,redirect,render_template,request
import pickle
import jsonify
import sklearn 
import requests
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np 
 
app = Flask(__name__)
with open('predict_productcount.pkl','rb') as f:
    model = pickle.load(f)

@app.route('/',methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        shop_id = int(request.form['shopid'])
        item_id = int(request.form['itemid'])

        prediction = model.predict([[shop_id,item_id]])
        output = prediction[0]
        return render_template('index.html',prediction_text="the predicted product count in month is  {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)