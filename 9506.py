while(True):
    n = int(input())
    li = []
    for i in range(1,n):
        if n%i ==0 :
            li.append(i)
    if n == sum(li):
        s = ' + '.join(list(map(str, li)))
        print(f'{n} = {s}')
    elif n == -1:
        break
    else :
        print(f"{n} is NOT perfect.")