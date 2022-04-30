def solution(skill, skill_trees):
    answer = 0
    result=0
    li = list(skill)
    for i in skill_trees:
        for j in i:
            for num in range(len(j)):
                if j[num] in li:
                    word = j[num] 
                
    answer=result
    return answer,word

skill = "CBD"
skill_trees=[["BACDE", "CBADF", "AECB", "BDA"]]
print(solution(skill,skill_trees))