import sys
N = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline())
cursor = len(N)
for _ in range(M):
    a = sys.stdin.readline().split()
    if a[0] == "P":
        N.insert(cursor,a[1])
        cursor+=1  
    elif a[0] == "L" :
        if cursor == 0:
            cursor = 0  
        else:
            cursor -= 1    
    elif a[0] == "D" :
        if cursor == len(N):
            cursor = len(N)    
        else :
            cursor += 1   
    elif a[0] == "B" :
        if cursor == 0:
            continue
        else:
            N.pop(cursor-1)
            cursor -= 1
for i in range(len(N)):
    print(N[i],end="")

        