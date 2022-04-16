n=int(input())
l=list(map(int,input().split()))
c=list(map(int,input().split()))
cost=c[0]*l[0]
min_c = c[0]
for i in range(1,len(l)):
    if c[i] <min_c:
       min_c=c[i]
    cost+=min_c*l[i]

print(cost)
