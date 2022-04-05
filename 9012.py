N = int(input())
for _ in range(N):
    a = list(input())
    result =0
    for i in range(len(a)):
        if a[i] =='('  :
            result += 1
        elif a[i] == ')' :
            result -= 1
        if result <0:
            print("NO")
            break
    if result >0:
        print("NO")
    elif result ==0 :
        print("YES")
    
    