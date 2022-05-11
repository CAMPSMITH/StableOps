import numpy as np

def APY_to_APR(APY, N):
    """
    Converts an APY value to APR
    
    Parameters:
    APY : the annual percentage yield (float)
    N : the number of compounding periods per year (int)
    """
    APR = N*(np.power((APY+1),1/N) - 1)
    return APR