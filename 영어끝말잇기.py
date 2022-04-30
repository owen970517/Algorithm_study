def solution(n, words):
    answer=[0,0]
    cnt=0
    li=[]
    li.append(words[0])
    for i in range(1,len(words)):
        cnt+=1
        if words[i] not in li and li[-1][-1] == words[i][0]:
            li.append(words[i])   
        else:
            answer[0] = (cnt %n)+1
            answer[1] = (cnt//n)+1
            cnt+=1
            break
    return answer
n = int(input())
words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n,words))
