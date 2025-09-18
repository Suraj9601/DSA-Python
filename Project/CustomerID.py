customer_ids = [101, 203, 345, 456, 567, 678, 789]
target = int(input("Enter the Customer ID you want to search: "))
n = 7

# Linear Search

def linear_search(customer_ids, target):
    for i in customer_ids:
        if i == target:
            return True
    return False

# Binary Search

def binary_search(customer_ids, target):
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        if customer_ids[mid] == target:
            return True
        elif customer_ids[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


print("Linear Search:", linear_search(customer_ids, target))
print("Binary Search:", binary_search(customer_ids, target))
