import pandas as pd

def stable_std(df):
    """
    Finds the standard deviation of the prices in a stable coin dataframe.
    
    Parameters:
    df : DataFrame containing a time series of prices for a stable coin (object: panda dataframe)
    
    Returns:
    stable_std[0] : a floating point standard deviation of the stable coin around 1 USD
    """
    
    mean = 1.0
    number = df.count()
    sqared_sum = df['prices'].apply(lambda x: (x - mean)**2).sum()
    stable_std = (sqared_sum/(number -1))**(1/2)
    return stable_std[0]      