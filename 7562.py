t=int(input())
count =0
dx = [2,-2,2,-2,1,-1,1,-1]
dy =[1,-1,-1,1,2,-2,-2,2]
for _ in range(t):
    l=int(input())
    start=input().split()
    end=input().split()
    for i in range(8):
        start[0]=int(start[0])+dx[i]
        start[1]=int(start[1])+dy[i]
        print(start[0],start[1])
        if start[0]>=1 and start[0] <=8 and start[1] >=1 and start[1]<=8:
            count +=1
print(count)

