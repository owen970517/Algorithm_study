def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        li=[]
        for j in i:
            if j in skill:
                li.append(j)
        for i in range(len(li)):
            if li[i] != skill[i]:
                break
        else:
            answer+=1
    return answer

skill = "CBD"
skill_trees=[["BACDE", "CBADF", "AECB", "BDA"]]
print(solution(skill,skill_trees))