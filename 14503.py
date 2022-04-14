# 0-3-2-1
dx =[-1,0,1,0]
dy =[0,1,0,-1]

def clean(r,c,d) :
    global count
    # 현재 위치 청소 
    if li[r][c] ==0 :
        li[r][c] = 2
        count +=1
    # 북 동 남 서 하나씩 회전
    for _ in range(4):
        nd = (d+3)%4
        nx = r +dx[nd]
        ny = c +dy[nd]
        if li[nx][ny]==0:
            clean(nx,ny,nd)
            return
        d = nd
    # 방향 뒤쪽으로 변경하고 이동  
    nd = (d+2)%4
    nx = r+dx[nd]
    ny = c+dy[nd]
    # 벽임 
    if li[nx][ny]==1:
        return
    # 방향을 뒤쪽으로 이동하기 위해 방향을 바꾼 것이기 때문에 구할 때는 기존 방향인 d를 사용
    clean(nx,ny,d)


n,m = map(int,input().split())
r,c,d = map(int,input().split())
li=[]
count = 0
for _ in range(n):
    a =list(map(int,input().split()))
    li.append(a)

clean(r,c,d)
print(count)