# 내가 푼 풀이 
# N,K = map(int,input().split())
# li=[]
# del_li = []
# for i in range(1,N+1):
#     li.append(i)
# while len(li) != 0:
#     if len(li) >2:
#         del_li.append(li.pop(K-1))
#         li=li[2:]+li[0:2]
#         print(li)
#     elif len(li) <=2:
#         del_li.append(li.pop(0))
#         print(li)
# print("<", ', '.join(str(i) for i in del_li), ">", sep="")

# 배운 풀이
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