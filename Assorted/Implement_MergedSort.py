# Implement a merge sort with recursion

def merge_sort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_arr = dataset[:mid]
        right_arr = dataset[mid:]

        print(left_arr, " ---", right_arr, "===", dataset)
        # recursively break down the arrays
        merge_sort(left_arr)
        merge_sort(right_arr)

        # now perform the merging
        i = 0  # index into the left array
        j = 0  # index into the right array
        k = 0  # index into merged array

        # while both arrays have content
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                dataset[k] = left_arr[i]
                i += 1
            else:
                dataset[k] = right_arr[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        # dataset = dataset + left_arr[i:]
        while i < len(left_arr):
            dataset[k] = left_arr[i]
            i += 1
            k += 1

        # dataset = dataset + right_arr[j:]

        # if the right array still has values, add them
        while j < len(right_arr):
            dataset[k] = right_arr[j]
            j += 1
            k += 1

        print("Now", left_arr, " ---", right_arr, "===", dataset)

        return dataset

# test the merge sort with data
items = [6, 20, 8, 19, 56, 23, 87, 2, 49, 1, 1]

print(items)
(merge_sort(items))
print(items)
