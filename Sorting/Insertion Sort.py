def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        curr = arr[i]
        prev = i-1
        
        while (prev >= 0 and arr[prev] > curr):
            arr[prev + 1] = arr[prev]
            prev -= 1
        
        arr[prev + 1] = curr
        
    return arr
arr = list(map(int,input("Enter array Elements : ").split()))
print("Original array:",arr)

sorted_arr = insertionSort(arr)
print("Sorted array : ",sorted_arr)