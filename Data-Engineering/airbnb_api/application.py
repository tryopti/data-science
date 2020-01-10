"""Flask App for Predicting Optimal AirBnB prices in Berlin"""
from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
import pickle
from joblib import load
from flask_cors import CORS
from flask_cors import cross_origin

# local import:
from .api_function import get_lemmas
from dotenv import load_dotenv
load_dotenv()

# create app:
def create_app():
    APP = Flask(__name__)
    CORS(APP)

    # load pipeline pickle:
    pipeline1 = load('airbnb_api/test3_regression.pkl')


    @APP.route('/', methods=['POST'])
    @cross_origin()
    def prediction():
        """
        Receives JSON request, creates dataframe with data,
        runs through predictive model, returns predicted price as JSON object.
        """

        # Receive data:
        listings = request.get_json(force=True)

        accommodates = listings["accommodates"]
        bathrooms = listings["bathrooms"]
        bedrooms = listings["bedrooms"]
        size = listings['size']
        room_type = listings["room_type"]
        bed_type = listings["bed_type"]
        minimum_nights = listings["minimum_nights"]
        instant_bookable = listings["instant_bookable"]
        cancellation_policy = listings["cancellation_policy"]
        bag_of_words = listings["bag_of_words"]


        features = {
        'accommodates': accommodates,
        'bathrooms': bathrooms,
        'bedrooms': bedrooms,
        'size': size,
        'room_type': room_type,
        'bed_type': bed_type,
        'minimum_nights': minimum_nights,
        'instant_bookable': instant_bookable,
        'cancellation_policy': cancellation_policy,
        'bag_of_words': bag_of_words
        }

        # Convert data into DataFrame:
        df = pd.DataFrame(listings, index=[1])
        # Uses NLP function to increase scores based on description given:
        df.bag_of_words = get_lemmas(df.bag_of_words.iloc[0])

        # Make prediction for optimal price:
        prediction = pipeline1.predict(df.iloc[0:1])
        # To work with backend's database (needed to be a float)
        output = float(prediction[0])

        # Return JSON object:
        return jsonify(int(output))

    return APP
