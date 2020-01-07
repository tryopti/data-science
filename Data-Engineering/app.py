"""Get started with flask app"""

from flask import Flask, jsonify, request
import pandas as pd
import pickle



def create_app():
    APP = Flask(__name__)


    @APP.route('/')
    def root():
        prediction = get_predictions()
        return jsonify(prediction)

    def get_predictions():
        # receive input
        listings = request.get_json(force=True)

        # get data from json:
        ## column = listings['column']

        # dictionary to format output for json:
        
        # model for predictions
return APP
