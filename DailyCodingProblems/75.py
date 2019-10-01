# Problem 75
# This problem was asked by Microsoft.

# Given an array of numbers, find the length of the longest increasing subsequence in the array.
# The subsequence does not necessarily have to be contiguous.

# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
# the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.cache = None

def get_subseq(arr, start):
    if start == len(arr):
        return 0

    current = arr[start]
    # print("\n", current)
    max_inc = 1
    for index in range(start + 1, len(arr)):
        # print(index)
        if arr[index] >= current:
            if index in cache:
                count = cache[index]
            else:
                count = get_subseq(arr, index) + 1
                cache[index] = count
            if count > max_inc:
                max_inc = count

    return max_inc


def get_subseq_helper(arr):
    global cache
    cache = dict()
    return get_subseq(arr, 0)

print(get_subseq_helper([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
