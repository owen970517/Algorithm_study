from itertools import combinations
import math


def solution(nums) :
    result=0
    li=[]
    new_li=[]
    for i in combinations(nums,3):
        li.append(i)
    for i in li:
        new_li.append(sum(i))
    for i in new_li:
        prime=True
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                prime=False
        if prime:
            result+=1
    answer=result
    return answer 
nums =[1,2,7,6,4]
#nums=[1,2,3,4]

print(solution(nums))