import numpy as np
from datetime import datetime,timezone
import pytz
import requests
import pandas as pd

def APY_to_APR(APY, N):
    """
    Converts an APY value to APR
    
    Parameters:
    APY : the annual percentage yield (float)
    N : the number of compounding periods per year (int)
    """
    APR = N*(np.power((APY+1),1/N) - 1)
    return APR


def epoch_to_datetime(epoch_time,time_zone_name='US/Eastern'):
    """Converts unix epoch time to date time
    If a time zone is provided, it will convert to that timezone.
    By default, time will be returned in US/Eastern time.
    If time_zone_name is set to None, it will return UTC time.
    This function is written to be imported into a notebook or other python program.
    If using Pandas, this function can be used in apply()

    Parameters:
        epoch_time (int): epoch time, must be an int
        time_zone_name (str): time zone name to localize time to, e.g. `US/Eastern`
    """
    epoch_time = int(epoch_time) # coerce to int in case is came in as a string
    dt = datetime.utcfromtimestamp(epoch_time) 
    dt = dt.replace(tzinfo=timezone.utc) # coerce to UTC for proper time zone conversion
    if time_zone_name is None:
        return dt # return UTC time
    # time zone set
    return dt.astimezone(pytz.timezone(time_zone_name))

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
    df.drop_duplicates(subset=['time'], keep='first', inplace=True)
    df.set_index('time', inplace=True)
    df.sort_index(inplace=True)
    return df
