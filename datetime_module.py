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
updated_date_time = my_date_time.replace(2050)
print(f"{updated_date_time}")

from datetime import date

date1 = date(2022,12,25)
date2 = date(2023,12,25)

difference_between_date = date2 - date1

print(f"The difference between {date2} and {date1} : {difference_between_date}")
