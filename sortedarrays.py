def merge_sorted_arrays(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    merged_array = [0] * (n1 + n2)
    i, j, k = 0, 0, 0

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            merged_array[k] = arr1[i]
            i += 1
        else:
            merged_array[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        merged_array[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        merged_array[k] = arr2[j]
        j += 1
        k += 1

    return merged_array

if __name__ == "__main__":
    arr1_input = input("Enter the elements of the first sorted array separated by spaces: ")
    arr1 = [int(n) for n in arr1_input.split()]
    arr2_input = input("Enter the elements of the second sorted array separated by spaces: ")
    arr2 = [int(n) for n in arr2_input.split()]

    resultingArray = merge_sorted_arrays(arr1, arr2)
    
    print("Merged Array:", resultingArray)
