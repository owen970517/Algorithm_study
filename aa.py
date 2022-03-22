def gcd(x, y):
    while x%y:
        x, y = y, x % y
    return y

T = int(input())
for i in range(T):
    a,b = map(int , input().split())
    GCD=gcd(a,b)
    LCM = (a*b)//GCD
    print(LCM)

