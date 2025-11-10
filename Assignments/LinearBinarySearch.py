customer_ids = [101, 502, 303, 404, 505, 606, 707, 808, 909]
target = int(input("Enter the customer ID to search: "))

# Linear Search
def linear_search(customer_ids, target):
    for i in range(len(customer_ids)):
        if customer_ids[i] == target:
            return i
    return -1


# Binary Search
def binary_search(customer_ids, target):
    customer_ids = sorted(customer_ids)
    left, right = 0, len(customer_ids) - 1
    while left <= right:
        mid = (left + right) // 2
        if customer_ids[mid] == target:
            return mid
        elif customer_ids[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


linear_result = linear_search(customer_ids, target)
print("Linear Search: Element found at index:", linear_result)
binary_result = binary_search(customer_ids, target)
print("Binary Search: Element found at index:", binary_result)
