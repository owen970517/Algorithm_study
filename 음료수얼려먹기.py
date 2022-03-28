def dfs(x,y):
    # 값이 범위를 벗어난 경우 취소
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    #현재 위치의 값이 0일 경우 1로 바꿔주고 상,하,좌,우에 대한 dfs 실행 
    if li[x][y]==0:
        li[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

N,M = map(int,input().split())
li=[]
for _ in range(N):
    a=list(map(int,input()))
    li.append(a)
print(li)
result = 0
for i in range(N):
    for j in range(M):
        if(dfs(i,j)==True):
            result +=1
print(result)