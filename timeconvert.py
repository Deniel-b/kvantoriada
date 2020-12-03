import time, datetime


time_tuple = (1956, 11, 12, 13, 59, 27, 2, 317, 0)
timestamp = time.mktime(time_tuple)
print(repr(timestamp))
