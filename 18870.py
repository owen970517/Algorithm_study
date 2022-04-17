# 딕셔너리를 활용하면 시간복잡도가 O(1) 
n=int(input())
x = list(map(int,input().split()))
li = list(set(x))
li.sort()
dic = {li[i] : i for i in range(len(li))}
print(dic)
for i in x:
    print(dic[i], end=" ")

# 내 풀이 이렇게 풀면 시간복잡도 O(N)이기 때문에 시간 초과가 발생 
# n=int(input())
# x = list(map(int,input().split()))
# a=x
# li = list(set(x))
# li.sort()
# for x in a:
#     print(li.index(x),end=" ")   
