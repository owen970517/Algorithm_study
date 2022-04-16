def fibonachi(n):
    if n>=2:
        return fibonachi(n-1) + fibonachi(n-2)
    elif n==1:
        return 1
    elif n==0:
        return 0
n = int(input())
print(fibonachi(n))