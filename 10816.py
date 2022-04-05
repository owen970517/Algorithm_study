def binary_search(arr , tar , start , end) :
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == tar :
            return count.get(tar)
        elif arr[mid] > tar :
            end = mid-1
            return binary_search(arr,tar,start,end)
        else:
            start = mid+1
            return binary_search(arr,tar,start,end)
    return 0


N = int(input())
a = list(map(int,input().split()))
sort_a = sorted(a)
M = int(input())
b = list(map(int,input().split()))

count = {}
for n in a:
    if n in count:
        count[n] +=1
    else :
        count[n] =1
print(count)
for i in range(M):
    print(binary_search(sort_a, b[i] ,0, len(sort_a)-1) , end=" ")
