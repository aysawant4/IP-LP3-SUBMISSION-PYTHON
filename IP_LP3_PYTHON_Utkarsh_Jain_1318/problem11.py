import datetime

yyyy,mm,dd=map(int,input().split(', '))
print(datetime.date(yyyy, mm, dd).isocalendar()[1])