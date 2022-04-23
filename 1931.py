n = int(input())
li=[]
for i in range(n):
    s= list(map(int,input().split()))
    li.append(s)
li.sort(key = lambda x: (x[1], x[0]))
print(li)
count=1
meeting_time = li[0][1]
for i in range(1,len(li)):
    if meeting_time<=li[i][0]:
        count+=1
        meeting_time = li[i][1]

print(count)

    