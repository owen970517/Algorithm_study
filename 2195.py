def copy(a,b):
    li.append(s[a-1:a+b-1])
    if b>1:
        c=s[a-1:a+b-1]
        li.append(c[::-1])
li=[]
s=input()
p=input()
print(copy(3,2))
print(copy(4,1))
print(copy(4,1))
print(copy(2,1))
print(copy(2,1))
print(copy(2,1))
print(copy(3,1))
print(copy(1,1))
print(copy(1,1))
print(copy(1,1))
for i in range(len(li)):
    print(li[i],end="")
