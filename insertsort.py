def insert_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while j>0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j-=1
a= [2,5,7,1,4,3,8,6,10,9]
insert_sort(a)
print(a)