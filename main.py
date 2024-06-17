from flask import Flask, render_template, request
from statsmodels.regression.linear_model import OLS
import statsmodels.regression.linear_model as smf
import pandas as pd
import numpy as np
import pickle

#initializing the app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact_us')
def contact():
    return render_template("contact.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/feedback')
def feedback():
    return render_template("feedback.html")

@app.route('/data', methods=['post'])
def get_data():
    try:
        print(request.form)
        income = int(request.form.get('income'))
        h_age = int(request.form.get('house age'))
        n_rooms = int(request.form.get('number of rooms'))
        n_bedrooms = int(request.form.get('number of bedrooms'))
        population = int(request.form.get('population'))

        # load the model
        load_model = pickle.load(open('USA_HousePredModel.pkl', 'rb'))
        data = data = {
                'Avg. Area Income': [income],
                'Avg. Area House Age': [h_age],
                'Avg. Area Number of Rooms': [n_rooms],
                'Avg. Area Number of Bedrooms': [n_bedrooms],
                'Area Population': [population]
                }

        test_data = pd.DataFrame(data)
        print("data", data, test_data)
        prediction = load_model.predict(test_data)

        print(prediction)
        response_str = ('Your Predicted House Price is:'+ prediction)
        return
    except ValueError as e:
        print("Invalid data:", type(e), e.args)


#run
app.run()