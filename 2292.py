n=int(input())
start_num=1
cnt=1
while n>start_num:
    start_num +=6*cnt
    cnt+=1
print(cnt)