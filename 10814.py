n=int(input())
li=[]
for _ in range(n):
    s=input().split()
    li.append(s)

sort_li = sorted(li,key=lambda x:int(x[0]))

for i in sort_li:
    print(i[0],i[1])
 
