
T = int(input())
A=0
B=0
C=0
if(T%10 != 0) :
    print(-1)
else :
    A += T//300
    T = T%300
    B += T//60
    T=T%60
    C += T//10
    T=T%10
    print(A,B,C,sep=" ")