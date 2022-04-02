li=[]
T = int(input())
for _ in range(T):
    a = int(input())
    li.append(a)
count = [0] *(max(li)+1)
for i in range(len(li)):
    count[li[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i ,end=" ")