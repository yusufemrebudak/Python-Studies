# import datetime # modul içindeki bütün class lar gelir 
from datetime import datetime
# from datetime import date # datetime modulundeki date class ını import ederiz.
# from datetime import time

result = dir(datetime) 

# print(result)    #['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
#  '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__',
#   '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date',
#    'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 
#    'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second',
#     'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 
# 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year'] datetime clası içindeki metodlar
simdi = datetime.now()
result=simdi.now() 
print(result) # 2021-02-19 12:14:00.919234
result=simdi.year
print(result) #2021 yazar
result=simdi.day
print(result) # 19 yazar
result=simdi.hour
print(result) # 12 saat şuan 12 olduğu için 12 yazar.
result=datetime.ctime(simdi)
print(result) # Fri Feb 19 12:16:28 2021 yazar.
result=datetime.strftime(simdi,'%Y')
print(result) # 2021
result=datetime.strftime(simdi,'%X')
print(result) # 12:18:26
result=datetime.strftime(simdi,'%d')
print(result) # 19
result=datetime.strftime(simdi,'%a')
print(result) # Fri 

result=datetime.strftime(simdi,'%Y %B %A')
print(result) # 2021 February Friday 

t = '15 Nisan 2019'
gun,ay,yil = t.split()
print(gun) # 21
print(ay) # Nisan
print(yil) # 2019


t = '15 April 2019 hour 10:12:34'
dt=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(dt) # 2019-04-15 10:12:34 yazdı 

birthday = datetime(1983,5,9,12,30,10)
print(birthday) # 1983-05-09 12:30:10 yazar.
result=datetime.timestamp(birthday)
print(result) # 421320610.0 saniye olarak getirilir.

