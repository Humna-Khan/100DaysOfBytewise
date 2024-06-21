def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

input_string = input("Enter the elements: ")
input = input_string.split()
array = [int(item) for item in input]
sorArray = quickSort(array)
print(sorArray)