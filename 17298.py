# 다른 사람이 짠 코드
import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
ans = [-1] * n
new_li = []
new_li.append(0)
for i in range(1, n):
    while new_li and li[new_li[-1]] < li[i]:
        ans[new_li.pop()] = li[i]
    new_li.append(i)
print(*ans)


#내가 푼 코드
# n=int(input())
# li = list(map(int,input().split()))
# ans=[]
# for i in range(n):
#     ai=li[i]
#     new_li=[]
#     for j in li[i+1:] :
#         if ai < j:
#             new_li.append(j)  
#     if len(new_li)==0:
#         ans.append(-1)
#     else :
#         ans.append(new_li[0])
# for i in ans:
#     print(i,end=" ")