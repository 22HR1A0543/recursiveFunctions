def sumOf(n):
    if n==0:
        return 0
    else:
        return n+sumOf(n-1)
n=int(input())
print(sumOf(n))
