def quickSort(arr, st, end):
    if st < end: 
        pivIdx = partition(arr, st, end)
        quickSort(arr, st, pivIdx - 1)   # left side
        quickSort(arr, pivIdx + 1, end)  # right side

def partition(arr, st, end):
    pivot = arr[end]
    idx = st - 1

    for j in range(st, end):
        if arr[j] <= pivot:
            idx += 1
            arr[idx], arr[j] = arr[j], arr[idx]

    arr[idx + 1], arr[end] = arr[end], arr[idx + 1]
    return idx + 1

arr = [4, 2, 7, 13, 8, 23]
quickSort(arr, 0, len(arr) - 1)
print("Sorted:", arr)
