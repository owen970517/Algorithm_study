n = int(input())
cnt =0
while n>=0:
    if n%5==0:
        cnt+=n//5
        print(cnt)
        break
    elif n//5 ==0 and n%3==1:
        print('-1')
        break
    n-=3
    cnt+=1