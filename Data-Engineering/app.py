"""Get started with flask app"""

from flask import Flask, jsonify, request
import pandas as pd
import pickle


APP = Flask(__name__)

# load model w/pickle


@APP.route('/')
def get_predictions():
        # get data
        listings = request.get_json(force=True)

        # convert data into dataframe

        # column = listings['column'] for each column

        # dictionary to format output for json

        # predictions

        # model for predictions

        # send back to browser
        output = {'results': int(result[0])}

        # return data
        return jsonify(results=output)

if __name__ == '__main__':
    APP.run()
