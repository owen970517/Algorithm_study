def binary_search(arr , tar , start , end) :
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == tar :
            return 1
        elif arr[mid] > tar :
            end = mid-1
        else:
            start = mid+1
    return 0

N = int(input())
A = list(map(int,input().split()))
sort_A = sorted(A)
M = int(input())
B = list(map(int,input().split()))

for i in range(M):
    print(binary_search(sort_A , B[i] ,0, len(sort_A)-1 ))
