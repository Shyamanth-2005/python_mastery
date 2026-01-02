# python has datetime module to handle date and time 
import datetime

print(dir(datetime))

import datetime as dt

print(dt.MAXYEAR)
print(dt.MINYEAR)
print(dt.UTC)


from datetime import datetime as dt

now = dt.now()
print(now) # 2026-01-02 18:02:55.548324

day = now.day
print(day) # 2

month = now.month
year = now.year
print(month,year)  # 1 2026

hour = now.hour
print(hour) # 18

minute = now.minute
print(minute) # 7

second = now.second
print(second) # 33

timestamp = now.timestamp()
print(timestamp)


print("{}-{}-{} {}:{}".format(day,month,year,hour,minute))
print(f"{day}/{month}/{year} {hour}:{minute}:{second}")

from datetime import datetime

today = datetime.today()
print(today)
