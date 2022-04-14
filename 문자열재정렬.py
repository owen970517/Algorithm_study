s = input()
li =[]
li2=[]
for i in s:
    # i가 알파벳인지 확인
    if i.isalpha():
        li.append(i)
        li.sort()
    # i가 숫자인지 확인
    elif i.isdigit():
        li2.append(i)
        li2.sort()
result = li+li2
for i in result:
    print(i,end="")