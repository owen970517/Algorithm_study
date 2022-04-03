N = int(input())
li = []
for _ in range(N) :
    a = input()
    if a not in li:
        li.append(a)
li.sort()
li.sort(key=len)
for i in li:
    print(i)