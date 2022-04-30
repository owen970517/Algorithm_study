def solution(d, budget):
    sum=0
    result=0
    sort_d = sorted(d)
    for i in sort_d:
        sum+=i
        if sum>budget:
            continue
        else:
            result+=1
    answer = result
    return answer

d = [1,3,2,5,4]
budget=9
print(solution(d,budget))