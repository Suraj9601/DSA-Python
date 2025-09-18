arr = [5, 3, 8, 6, 2]
print("Original List:", arr)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


print("\nChoose sorting method:")
print("1. Bubble Sort")
print("2. Selection Sort")

choice = input("Choose Option (1 or 2) : ")
print()

if choice == "1":
    bubble_sort(arr)
    print("Bubble Sort result:", arr)
elif choice == "2":
    selection_sort(arr)
    print("Selection Sort result:", arr)
else:
    print("Invalid choice.")
