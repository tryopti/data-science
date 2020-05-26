import pandas as pd
import numpy as np
import math

# Can also provide regular expression version.
# This was simpler.
#TODO Provide case checking. 
def dict_length(dict):
    """Return series object."""
    for i in range(0, len(listings_summary['amenities'])):
        if math.isnan(listings_summary['amenities'][i]):
            print("NaN has been found")

    for i in range(0, len(dict)):
        dict[i] = dict[i].strip('{}');
        dict[i] = dict[i].strip(',')
        dict[i] = dict[i].count(",")
    return dict
