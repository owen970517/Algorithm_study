n,m=map(int,input().split())
for i in range(n,m):
    for j in range(n,m):
        if j%i ==0:
            print(j)

