N = int(input())
li=[]
for _ in range(N):
    a = int(input())
    li.append(a)
sort_li = sorted(li)
for i in range(len(sort_li)):
    print(sort_li[i])
