arr = [1, 2, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10]
arr.sort()  # Binary search requires sorted array
print("Sorted array:", arr)

target = int(input("Enter the Element you want to search: "))

def binary(arr, target):
    

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

index = binary(arr, target)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found.")
