"""Get started with flask app"""

from flask import Flask, jsonify, request
import pandas as pd
import pickle


APP = Flask(__name__)

# load model w/pickle


@APP.route('/')
def get_predictions(bedrooms, bathrooms, square_feet, longitude, latitude,
                    description, accommodates):
        # get data
        listings = request.get_json(force=True)

        # column = listings['column'] for each column
        # MAY NEED TO CHANGE COLUMNS
        bedrooms = listings['bedrooms']
        bathrooms = listings['bathrooms']
        square_feet = listings['square_feet']
        longitude = listings['longitude']
        latitude = listings['latitude']
        description = listings['description']
        accommodates = listings['accommodates']

        # dictionary to format output for json
        features = {'bedrooms':bedrooms, 'bathrooms': bathrooms,
                    'square_feet':square_feet, 'longitude': longitude,
                    'latitude': latitude, 'description': description,
                    'accommodates': accommodates}

        # convert data into dataframe
        df = pd.DataFrame(listings)

        # predictions

        # model for predictions

        # send back to browser
        output = {'results': int(result[0])} # not sure about this

        # return data
        return jsonify(results=output)

if __name__ == '__main__':
    APP.run()
