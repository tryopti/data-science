import pandas as pd
import numpy as np

# Can also provide regular expression version.
# This was simpler.
#TODO Provide case checking. 

def dict_length(dict):
    """Return series object."""
    for i in range(0, len(dict)):
        dict[i] = dict[i].strip('{}');
        dict[i] = dict[i].strip(',')
        dict[i] = dict[i].count(",")
    return dict

