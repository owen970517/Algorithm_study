T = int(input())
Yonsei = 0
Korea = 0
for _ in range(T):
    for _ in range(9):
        Y,K = map(int,input().split())
        if Y > K:
            Yonsei +=1
        elif Y == K :
            Yonsei = Yonsei
            Korea = Korea
        else :
            Korea +=1
if Yonsei > Korea:
    print("Yonsei")
elif Yonsei == Korea:
    print("Draw")
else :
    print("Korea")