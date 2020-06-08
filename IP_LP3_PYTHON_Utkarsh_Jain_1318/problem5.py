x=input()
newdict={}
for y in x:
    if(y in newdict):
        newdict[y]+=1
    else:
        newdict[y]=1
for letter in newdict:
    print(letter,end="")