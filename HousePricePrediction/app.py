# flask, scikit-learn, pandas, pickle-mixin, flask-cors

import pandas as pd
from flask import Flask,render_template,request
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
data=pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open('RidgeModel.pkl','rb'))


@app.route('/')
def index():  # put application's code here
    locations= sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict',methods=['POST'])
def predict():
    locations = request.form.get('location')
    bhk= float(request.form.get('bhk'))
    bath= float(request.form.get('bath'))
    sqft= request.form.get('total_sqft')
    print(locations,bhk,bath,sqft)
    input= pd.DataFrame([[locations,bhk,bath,sqft]], columns=['location','bhk','bath','total_sqft'])
    prediction=pipe.predict(input)[0] * 1e5 #list with one val [0]  =ans (int returned)
    return str(np.round(prediction, 2))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
