#CODING QUESTIONS:10
#Write a Python program to sort a list of elements using the selection sort algorithm.
A=list(map(int, input().split()))
for i in range(len(A)):

    # Finding the minimum element in remaining unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    #Swaping the found minimum element with the first element
    A[i], A[min_idx] = A[min_idx], A[i]
print(A)