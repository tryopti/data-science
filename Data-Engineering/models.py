# NOT NEEDED

from flask_sqlalchemy import SQLAlchemy
from .app import DB


class User(DB.Model):
    """
    AirBnB host
    """
    id = DB.Column(DB.BigInteger, primary_key=True)
    user_name = DB.Column(DB.String(20))


class Listing(DB.Model):
    """
    AirBnB listings to predict
    """
    id = DB.Column(BigInteger, primary_key=True)
    accommodations = DB.Column(DB.BigInteger)
    bathrooms = DB.Column(DB.BigInteger)
    rooms = DB.Column(DB.BigInteger)
    neighborhood = DB.Column(DB.Unicode(200))
    room_type = DB.Column(DB.Unicode(200))
    # add or remove columns as needed
    def __repr__(self):
        return '<Listing {}>'.format(self.name)
