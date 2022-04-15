n = int(input())
s = list(map(int,input().split()))
s.sort()
li=[]
for _ in range(n):
    a=s.pop(0)+s.pop(len(s)-1)
    li.append(a)
print(min(li))