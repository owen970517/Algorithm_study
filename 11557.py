T = int(input())
for _ in range(T):
    N = int(input())
    M =0
    U=""
    for _ in range(N):
        S,L = input().split()
        if(int(L)>M):
            M=int(L)
            U = S
    print(U)