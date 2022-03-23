a = list(input())
print(a)
sum = 0
for i in range(len(a)):
    if i ==0 :
        sum = 10
    elif a[i-1] == a[i]:
        sum +=5
    else :
        sum +=10
print(sum)
