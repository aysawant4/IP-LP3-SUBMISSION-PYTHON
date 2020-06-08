n=int(input())
words={}
for i in range(0,n):
    String=input()
    if(String in words):
        words[String]+=1
    else:
        words[String]=1

print(len(words))
for x in words:
    print(words[x],end=" ")