def dfs(x,y):
    global cnt
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
    if li[x][y]==1:
        li[x][y] = 2
        cnt+=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

N = int(input())
li=[]
ans=[]
cnt=0
result = 0
for _ in range(N):
    a=list(map(int,input()))
    li.append(a)

for i in range(N):
    for j in range(N):
        if(dfs(i,j)==True):
            ans.append(cnt)
            result +=1
            cnt=0
ans.sort()
print(result)
for i in ans:
    print(i)
