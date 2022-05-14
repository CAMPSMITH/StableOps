import requests
import json
import pandas as pd
import os
import numpy as np
from time_utils import epoch_to_datetime


def extract_epoch_time(item):
        # item is expected to be an array where the 1st element in the array is the epoch time.
        # this function returns the epoch time.
    return item[0]
    
def extract_value(item):
        # item is expected to be an array where the 2nd element in the array is the value.
        # this function returns the value.
    return item[1]
    
    
def coin_gecko_cleaner(url_to_coin):
    """
    Converts Coin Gecko's URL to a clean dataframe.
    
    Parameters:
        url_to_coin (str): Coin Gecko's API url string, must be a str
    """
    coin_response = requests.get(url_to_coin).json()
    df = pd.DataFrame(coin_response)
    df['time'] = df['prices'].apply(extract_epoch_time)
    df['prices']= df['prices'].apply(extract_value)
    df['market_caps']=df['market_caps'].apply(extract_value)
    df['total_volumes']=df['total_volumes'].apply(extract_value)
    df['time'] = df['time']/1000
    df['time']=df['time'].apply(epoch_to_datetime)
    df['time'] = df['time'].dt.date
    df.set_index('time', inplace=True)
    return df

