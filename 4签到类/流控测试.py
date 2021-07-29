import datetime
import time

def timeChanged(dt):
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timeStamp = time.mktime(timeArray)
    return timeStamp







while time.time() < timeChanged("2021-07-26 16:47:00"):
    print(datetime.datetime.now().strftime('%H:%M:%S'))
    time.sleep(20)

