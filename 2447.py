def star(n):
    for i in range(n):
        for j in range(i,n):
            print('*' ,end="")
n = int(input())
star(n)