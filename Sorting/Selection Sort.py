# Time Complexity is O(n²)
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        smallestIdx = i
        for j in range(i+1,n):
            if arr[j] < arr[smallestIdx]:
                smallestIdx = j
        arr[i],arr[smallestIdx] = arr[smallestIdx],arr[i]
    return arr

arr = list(map(int,input("Enter array Elements : ").split()))
print("Original array:",arr)

sorted_arr = selectionSort(arr)
print("Sorted array : ",sorted_arr)