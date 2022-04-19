import sys

n=int(sys.stdin.readline())
li=[0]*10001

for _ in range(n):
    s=int(sys.stdin.readline())
    li[s]+=1
for i in range(len(li)):
    if li[i] !=0:
        for j in range(li[i]):
            print(i)

#카운팅 정렬을 이용한 방법
# n= int(sys.stdin.readline())
# arr=[]
# for _ in range(n):
#     s=int(sys.stdin.readline())
#     arr.append(s)

# count = [0] * (max(arr) + 1)

# for num in arr:
#     count[num] += 1
    
# for i in range(1, len(count)):
#     count[i] += count[i-1]

# result = [0] * (len(arr))

# for num in arr:
#     idx = count[num]
#     result[idx - 1] = num
#     count[num] -= 1
# for i in result:
#     print(i)

#딕셔너리를 활용한 방법
# arr = [5,2,3,1,4,2,3,5,1,7]

# count_dict = {}

# for num in arr:
#     if num in count_dict:
#         count_dict[num] += 1
    
#     else:
#         count_dict[num] = 1

# result = []

# for num in range(max(arr) + 1):
#     while num in count_dict and count_dict[num] != 0:
#         result.append(num)
#         count_dict[num] -= 1

# print(result)