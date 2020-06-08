#CODING QUESTIONS:5
a=str(input())
b=set()
for x in a:
    if x not in b:
        b.add(x)
        print(x,end="")
