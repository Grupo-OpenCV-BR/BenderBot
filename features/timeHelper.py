from datetime import datetime
import time
import pytz

def get_actual_time():
    time_zone = pytz.timezone('Brazil/East')
    unix_time = int(time.time())
    actual_time = datetime.fromtimestamp(unix_time, time_zone)
    return actual_time.hour

def get_unix_time():
    return int(time.time())