data  = input().split() 
a = int(data[0])
b = int(data[1])
 
def gcd(a, b):
    if (a == 0): 
        return b; 
    return gcd(b%a, a); 
 

count = 1
for i in range(2, gcd(a, b)+1):
    if a%i==0 and b%i==0:
        count = count+1
print(count)