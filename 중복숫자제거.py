def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i==0:
            answer.append(arr[i])
        elif answer[-1] != arr[i]:
            answer.append(arr[i])
    
    return answer

arr=[1,1,3,3,0,1,1]
print(solution(arr))