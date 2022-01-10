from datetime import date, time, datetime, timedelta

today = date.today()
etime = timedelta(hours=1)
print("Today is {},{} ,{}".format(today.year, today.month, today.day))
print("Now is {}".format(etime.seconds))
