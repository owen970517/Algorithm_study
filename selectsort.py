def selection_sort(arr):
    for i in range(len(arr) ):
        m =999
        for j in range(i,len(arr)):
            if m> arr[j]:
                m=arr[j]
                min_idx = j
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
a= [2,5,7,1,4,3,8,6,10,9]
print(len(a))
selection_sort(a)
print(a)

