def smallest(arr, n):
    arr.sort()
    smallest = arr[n - 1]
    return smallest
print(smallest([10,6,22, 43, 2, 7],2))