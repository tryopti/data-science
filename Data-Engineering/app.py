"""Get started with flask app"""

from flask import Flask, jsonify, request
import pandas as pd
import pickle

from .predict import get_prediction


def create_app():
    APP = Flask(__name__)


    @APP.route('/')
    def root():
        prediction = get_prediction()
        return jsonify(prediction)

return APP
