import datetime

mytime = datetime.time(10,10,10,10)
print(mytime)
print(f"Hour:{mytime.hour} Minute:{mytime.minute} Second:{mytime.second} Microsecond:{mytime.microsecond}")

today = datetime.date.today()
print(f"{today}")
print(f"{today.ctime()}")


