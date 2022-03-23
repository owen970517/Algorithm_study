N = int(input())
li=[]
for _ in range(N):
    a, b, c = map(int, input().split())
    money = 0
    if a == b == c:
        money = 10000+(a*1000)
        li.append(money)
        
    elif a == b or a == c:
        money = 1000+(a*100)
        li.append(money)
        
    elif b == c:
        money = 1000+(b*100)
        li.append(money)
        
    else:
        money = 100 * max(a,b,c)
        li.append(money)
        
print(max(li))