#CODING QUESTIONS:11
#Write a Python program to get a week number
import datetime
yy=int(input("Enter year \n"))
mm=int(input("Enter month \n"))
dd=int(input("Enter day \n"))
c=datetime.date(yy,mm,dd)
d=c.isocalendar()[1]      #[1] is for week number
print(d)