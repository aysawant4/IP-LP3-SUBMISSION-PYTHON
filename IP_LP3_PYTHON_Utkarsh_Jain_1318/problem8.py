def sum_series(n):
    answer=0
    while(n>=0):
        answer+=n
        n=n-2
    return answer
n=int(input())

print(sum_series(n))