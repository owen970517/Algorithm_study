N = int(input())
li=[]
for _ in range(N):
    a,b = map(int,input().split())
    li.append([b,a])
li.sort()
for i in li:
    print(i[1],i[0])

