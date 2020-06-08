#CODING QUESTIONS:3

from collections import Counter
#initializing count
count=0

#taking number of inputs form user
n=int(input("enter integer"))

#initializing words array
words=[]

#filling the words array from user
while n>0:
    words.append(str(input()))
    n-=1

#'Counter' is used to count the keys and values. it removes any duplicates. As in it creates a dictionary.
c=Counter(words)

#prints the length of dictionary
print(len(c))

#To print the values
for (i,j) in c.items():
    print(j, end=" ")       #end=" " is used to print on same line

