from telegram.utils.helpers import from_timestamp
import time
import pytz


def get_actual_time():
    time_zone = pytz.timezone('Brazil/East')
    unix_time = int(time.time())    
    actual_time = from_timestamp(unix_time, time_zone)

    return actual_time.hour

def get_unix_time():
    unix_time = int(time.time())   
    return unix_time