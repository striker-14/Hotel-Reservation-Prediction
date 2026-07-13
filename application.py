# Write your Flask code here
import joblib # for loading our model for prediction
import numpy as np
from config.paths_config import MODEL_OUTPUT_PATH
from flask import Flask, render_template,request

app = Flask(__name__) # initializing Flask

loaded_model = joblib.load(MODEL_OUTPUT_PATH) # load model

@app.route('/',methods=['GET','POST']) # set up route (route will basically be the home page) | We used both GET and POST because we will be getting data from the website and then we will post data from Flask to that website only
def index():
    if request.method=='POST':

        # getting the data
        lead_time = int(request.form["lead_time"])
        no_of_special_request = int(request.form["no_of_special_request"])
        avg_price_per_room = float(request.form["avg_price_per_room"])
        arrival_month = int(request.form["arrival_month"])
        arrival_date = int(request.form["arrival_date"])

        market_segment_type = int(request.form["market_segment_type"])
        no_of_week_nights = int(request.form["no_of_week_nights"])
        no_of_weekend_nights = int(request.form["no_of_weekend_nights"])

        type_of_meal_plan = int(request.form["type_of_meal_plan"])
        room_type_reserved = int(request.form["room_type_reserved"])


        # convert all this data into a numpy array
        features = np.array([[lead_time,no_of_special_request,avg_price_per_room,arrival_month,arrival_date,market_segment_type,no_of_week_nights,no_of_weekend_nights,type_of_meal_plan,room_type_reserved]])

        prediction = loaded_model.predict(features) # doing prediction

        return render_template('index.html', prediction=prediction[0]) # return result (render_template helps to show result on our HTML page)
    
    return render_template("index.html" , prediction=None) # if you're not getting any input, then also you HTML file should be running

if __name__=="__main__":
    app.run(host='0.0.0.0' , port=8080)