def arithmetic(li):
    sum=0
    for i in li:
        sum+=i
    print(round((sum/len(li))))
def center(li):
    li.sort()
    print(li[round(len(li)/2)])
def mode(li):
    dic={}
    a=[]
    result=[]
    for i in li:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in dic:
        a.append([i,dic[i]])
    for i in range(len(a)):
        if len(a)==1:
            result.append(a[i][0])
        elif a[i][1] == max(a[1]):
            result.append(a[i][0])
    if len(result) != 1:
        print(result[1])
    else:
        print(result[0])

def scope(li) :
    a=max(li)
    b=min(li)
    print(a-b)         
n=int(input())
li=[]
for _ in range(n):
    s=int(input())
    li.append(s)
arithmetic(li)
center(li)
mode(li)
scope(li)