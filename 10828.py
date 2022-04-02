import sys


N = int(sys.stdin.readline())
li = []
for _ in range(N):
    a = sys.stdin.readline().split()
    if a[0] == "push" :
        li.append(a[1])
    elif a[0] == "top" :
        if len(li) == 0:
            print(-1)
        else :
            print(li[-1])
    elif a[0] == "size" :
        print(len(li))
    elif a[0] == "empty":
        if len(li) == 0 :
            print(1)
        else : 
            print(0)
    elif a[0] == "pop":
        if len(li) ==0:
            print(-1)
        else :
           print(li.pop())
        