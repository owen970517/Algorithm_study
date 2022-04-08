s=input()
cnt =0
for i in s:
    if i =='1' :
        i=0
        cnt +=1
print((cnt//2)-1)