arr = [26000, 25000, 52000, 10000, 42000, 15000]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        smallestIdx = i
        for j in range(i+1,n):
            if arr[j] < arr[smallestIdx]:
                smallestIdx = j
        arr[i],arr[smallestIdx] = arr[smallestIdx],arr[i]
    return arr

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

print("1) Selection Sort \n2) Bubble Sort")
choice = int(input("Enter the choice : "))

if choice == 1:
    print(selectionSort(arr))
else:
    print( bubbleSort(arr))