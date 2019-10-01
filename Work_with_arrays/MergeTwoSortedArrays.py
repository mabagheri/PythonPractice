"""
Given two sorted arrays, the task is to merge them in a sorted manner.
https://www.geeksforgeeks.org/merge-two-sorted-arrays/
"""

def mergeArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    sorted_array = []
    i = j = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1

    while i < n1:
        sorted_array.append(arr1[i])
        i += 1

    while j < n2:
        sorted_array.append(arr2[j])
        j += 1

    return sorted_array


# Driver code
array1 = [1, 4, 5, 8, 10]

array2 = [2, 4, 6, 8]
print(mergeArrays(array1, array2))
