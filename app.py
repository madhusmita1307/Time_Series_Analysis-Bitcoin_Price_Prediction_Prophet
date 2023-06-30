import numpy as np
import pandas as pd
from flask import Flask, render_template,request, jsonify
import pickle

app = Flask(__name__)
crypto = pickle.load(open('crypto.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Bitcoin', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/predict_page', methods=['GET'])
def predict():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def y_predict():
    future = crypto.make_future_dataframe(periods=365)
    forecast = crypto.predict(future)

    if request.method == "POST":
        ds = request.form.get("Date", "")
        if ds:
            print(ds)
            ds = str(ds)
            print(ds)
            next_day = ds
            print(next_day)
            prediction = forecast[forecast['ds'] == next_day]['yhat'].item()
            prediction = round(prediction, 2)
            print(prediction)
            return render_template('predict.html', prediction_text="Bitcoin Price on the selected date {} is $ {} cents".format(ds, prediction))

    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)