

N,M = map(int,input().split())
li=[]
for _ in range(N):
    a=list(map(int,input()))
    li.append(a)
print(li)
result=0
for i in range(N):
    for j in range(M):
        if li[i][j] ==1:
            result +=1
print(result)
