N,K = map(int,input().split())
li=[]
del_li = []
for i in range(1,N+1):
    li.append(i)
while len(li) != 0:
    if len(li) >2:
        del_li.append(li.pop(K-1))
        li=li[2:]+li[0:2]
        print(li)
    elif len(li) <=2:
        del_li.append(li.pop(0))
        print(li)
print("<", ', '.join(str(i) for i in del_li), ">", sep="")
