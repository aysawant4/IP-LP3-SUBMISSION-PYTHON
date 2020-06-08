#CODING QUESTIONS:6b
print("1. C to F\n2. F to C")
x=int(input("Select from options:\t"))

if x==1:
    c=int(input("Enter temperature in Celsius:\t"))
    f=(c*9/5)+32
    print(c,end="")
    print("°C is",round(f),"in Fahrenheit")
elif x==2:
    f=int(input("Enter temperature in Fahrenheit:\t"))
    c=(f-32)*5/9
    print(f,end="")
    print("°F is",round(c),"in Celsius")
else:
    print("Select correct option")