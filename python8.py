"""
#
# Part: python datetime
#
"""

from datetime import datetime,date,time

x = datetime.now()
print(x)
print(x.strftime("%Y-%M-%D %H-%M-%S"))
print(x.day)
print(x.month)
print(x.year)
print(x.hour)
print(x.minute)
print(x.second)