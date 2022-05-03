n = int(input())
x,y=0,0
plans=input().split()
count=0
dx = [0,0,-1,1]
dy=[-1,1,0,0]
e=[]
s=[]
move_types = ['D','U','L','R']

for plan in plans:
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x +dx[i]
            ny= y+dy[i]
            if nx>5 or nx <-5 or ny >5 or ny<-5:
                continue
            if (x,y) in s and (nx,ny) in e:
                x,y=nx,ny
                continue
            count +=1
            s.append((x,y))
            e.append((nx,ny))
            x,y=nx,ny
print(nx,ny,count)

for i in s,e:
    print(i)