n = int(input())
A=100
B=100
for _ in range(n):
    a,b = map(int,input().split())
    if a<b:
        A=A-b
    elif a==b:
        A=A
        B=B
    else :
        B = B-a
print(A)
print(B)