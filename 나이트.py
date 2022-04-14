n = input()
print(n[0],n[1])
x,y = 1,1
count =0
dx = [2,-2,2,-2,1,-1,1,-1]
dy =[1,-1,-1,1,2,-2,-2,2]

for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx>=1 and nx <=8 and ny >=1 and ny<=8:
        count +=1
print(count)