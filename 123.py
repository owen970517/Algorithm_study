from math import gcd

T = int(input())
GCD = 0
LCM = 0
for i in range(T) :
    a,b = map(int, input().split())
    if(a%b == 0) :
        GCD = a
    else :
        GCD = gcd(b,a%b)
    LCM = (a*b)//GCD
    print(LCM)