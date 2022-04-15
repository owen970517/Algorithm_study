n=int(input())

for _ in range(n):
    quater=0
    dime=0
    nickel=0
    penny=0
    c = int(input())
    quater+=c//25
    c%=25
    dime+=c//10
    c%=10
    nickel+=c//5
    c%=5
    penny+=c//1
    print(quater,dime,nickel,penny,end=" \n")