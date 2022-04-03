import sys
N = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline())
li=[]
for _ in range(M):
    a = sys.stdin.readline().split()
    if a[0] == "P":
        N.append(a[1])
    elif a[0] == "L":
        if len(N) != 0:
            li.append(N.pop())
    elif a[0] == "B":
        if len(N) ==0:
            continue
        else :
            N.pop()
    elif a[0] == "D":
        if len(li) !=0 :
            N.append(li.pop())

for i in range(len(N)):
    print(N[i] , end="")
for j in reversed(range(len(li))):
    print(li[j],end="")
