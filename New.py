import datetime

time_now = datetime.datetime.now()
default_datetime = datetime.datetime(2021, 5, 12, 7, 29, 16)
if time_now > default_datetime: print('yes')
else: print("no")

# print(default_datetime)
# print(time_now)
# print(default_datetime-time_now)
# time_diff = default_datetime-time_now
# print(time_diff.seconds/3600)