def merge(arr, st, mid, end):
    i = st
    j = mid + 1
    temp = []
    
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    while i <= mid:
        temp.append(arr[i])
        i += 1
    
    while j <= end:
        temp.append(arr[j])
        j += 1
    
    for idx in range(len(temp)):
        arr[st + idx] = temp[idx]

def mergeSort(arr, st, end):
    if st < end:
        mid = (st + end) // 2
        mergeSort(arr, st, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, st, mid, end)
    return arr

arr = [2, 4, 75, 32, 12, 8, 23]
print("Original:", arr)

sorted_arr = mergeSort(arr, 0, len(arr) - 1)
print("Sorted  :", sorted_arr)
