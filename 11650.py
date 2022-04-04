N = int(input())
li=[]
for _ in range(N):
    a,b = map(int,input().split())
    li.append([a,b])
print(li)
li.sort()
for i in range(N):
    print(li[i][0],li[i][1])

