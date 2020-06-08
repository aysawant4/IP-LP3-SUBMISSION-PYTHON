#CODING QUESTIONS:2
def leap(x):
    if x % 4 == 0 and x % 100 != 0:
        return True
    elif x % 400 == 0 and x % 100 == 0:
        return True
    elif (x % 100 == 0):
        return False

y=int(input("Enter the year between 1900 and 10"))
m=bool(leap(y))
print(m)

