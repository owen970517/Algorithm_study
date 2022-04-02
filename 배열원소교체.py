#내가 푼 방법
N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for _ in range(K):
    if min(A) < max(B) :
        a = max(B)
        b = min(A)
        A.remove(min(A))
        B.remove(max(B))
        A.append(a)
        B.append(b)
print(A)
print(B)

# 정답 
# N,K = map(int,input().split())
#A = list(map(int,input().split()))
#B = list(map(int,input().split()))
#A.sort() 오름차순으로 A 배열을 정렬 
#B.sort(reverse=True) B배열을 내림 차순으로 정렬 
#for i in range(K): 
#   if A[i] < B[i] :
#       A[i],B[i] = B[i] , A[i]

#



