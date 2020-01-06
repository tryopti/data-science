from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Listing(DB.Model):
    """
    AirBnB listings to predict
    """
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.Unicode(200), nullable=False)
    host_id = DB.Column(DB.BigInteger, primary_key=True)
    host_name = DB.Column(DB.Unicode(200), nullable=False)
    neighborhood = DB.Column(DB.Unicode(200))
    room_type = DB.Column(DB.Unicode(200))
    # add or remove columns as needed
    def __repr__(self):
        return '<Listing {}>'.format(self.name)
