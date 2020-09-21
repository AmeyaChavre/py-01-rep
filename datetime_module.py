import datetime

mytime = datetime.time(10,10,10,10)
print(mytime)
print(f"Hour:{mytime.hour} Minute:{mytime.minute} Second:{mytime.second} Microsecond:{mytime.microsecond}")

today = datetime.date.today()
print(f"{today}")
print(f"{today.ctime()}")

from datetime import datetime

my_date_time = datetime(2028,10,30,15,21,2,29)

print(f"{my_date_time}")
