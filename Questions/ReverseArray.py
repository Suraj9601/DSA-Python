arr = [1, 2, 4, 5,  6, 7, 8, 9, 10]
print(arr)

def reverse(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[right],arr[left] = arr[left],arr[right]
        left += 1
        right -= 1

reverse(arr)
print(arr)