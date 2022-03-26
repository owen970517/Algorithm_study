N = int(input())
li=[]
for _ in range(N):
    v = int(input())
    li.append(v)
    if li.count(0) > li.count(1):
        result = "Junhee is not cute!"
    else :
        result = "Junhee is cute!"
print(result)