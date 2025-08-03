def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        isSwap = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                isSwap = True
        if not isSwap:
            break
    return arr

arr = list(map(int,input("Enter array Elements : ").split()))
print("Original array:",arr)

sorted_arr = bubbleSort(arr)
print("Sorted array : ",sorted_arr)