def selectionSort(arr):
    n = len(arr)

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]

n = int(input("Enter the size of the input: "))
arr = []
print("Enter the elements of the array:")
for i in range(n):
    element = int(input("Enter the {} element: ".format(i+1)))
    arr.append(element)

print("Unsorted array:")
for num in arr:
    print(num, end=" ")

selectionSort(arr)

print("\nSorted array:")
for num in arr:
    print(num, end=" ")
