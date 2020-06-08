
def SelctionSort(A):
    for i in range(len(A)):
        minindex = i 
        for j in range(i+1, len(A)): 
            if A[minindex] > A[j]: 
                minindex = j        
        A[i], A[minindex] = A[minindex], A[i] 
    
A=[int(item) for item in input("Enter the numbers:").split()]
SelctionSort(A)
print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i],end=" ")