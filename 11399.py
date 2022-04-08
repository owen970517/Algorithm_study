N = int(input())
P = list(map(int,input().split()))
P.sort()
sum=0

for i in range(N):
    if i==0:
        sum += P[i]
        b = P[i]
    else:
        b += P[i]
        sum += b
print(sum)