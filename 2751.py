import sys

n= int(sys.stdin.readline())
li=[]
for _ in range(n):
    s=int(sys.stdin.readline())
    li.append(s)
li.sort()
for i in li:
    print(i)