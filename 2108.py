import sys

def arithmetic(li):
    sum=0
    for i in li:
        sum+=i
    avg=round((sum/len(li)))
    return avg
def center(li):
    center= li[len(li)//2]
    return center
def mode(li):
    dic={}
    for i in li:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    modes = [ k for k, v in dic.items() if v == max(dic.values())]
    if len(modes) > 1:
        return modes[1]
    else:
        return modes[0]

def scope(li) :
    a=max(li)
    b=min(li)
    scope=a-b
    return scope        
n=int(sys.stdin.readline())
li=[]
for _ in range(n):
    s=int(sys.stdin.readline())
    li.append(s)
li.sort()
print(arithmetic(li))
print(center(li))
print(mode(li))
print(scope(li))