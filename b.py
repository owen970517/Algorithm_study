from collections import deque
N,K= map(int, input().split())

q = deque(range(1, N+1))
del_li = []
while len(q) != 1:
    for _ in range(K-1):
        q.append(q.popleft())
    del_li.append(q.popleft())
del_li.append(q[0])

print("<", ', '.join(str(i) for i in del_li), ">", sep="")