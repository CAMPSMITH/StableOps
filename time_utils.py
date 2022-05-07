from datetime import datetime,timezone
import pytz

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

    
if __name__ == ('__main__'):
    # confirm epoch time conversion with https://www.utilities-online.info/epochtime
    print(epoch_to_datetime(1651937236).strftime('%Y-%m-%d %H:%M:%S %z'))
    