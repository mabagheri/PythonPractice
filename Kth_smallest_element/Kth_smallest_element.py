"""## Find nth smallest element in numpy array"""

# https://stackoverflow.com/questions/22546180/find-nth-smallest-element-in-numpy-array
# https://codereview.stackexchange.com/questions/201241/k-th-smallestelement-in-unsorted-array-in-python

import numpy as np
import heapq
import sys


def find_nth_smallest_old_way(a, n):
    return np.max(np.partition(a, n)[:n])


# Solution suggested by Jaime and HYRY
def find_nth_smallest_proper_way(a, n):
    return np.partition(a, n - 1)[n - 1]


# ----------------------------------------------------------------------------------------------------------------------------
# https://codereview.stackexchange.com/questions/201241/k-th-smallestelement-in-unsorted-array-in-python
# https://www.youtube.com/watch?v=eaYX0Ee0Kcg
def kthSmallest_byHeap(iterable, k):
    smallest = []
    for value in iterable:
        if len(smallest) < k:
            heapq.heappush(smallest, -value)
        else:
            heapq.heappushpop(smallest, -value)
    if len(smallest) < k:
        return None
    return -smallest[0]


# ----------------------------------------------------------------------------------------------------------------------------
# https://stackoverflow.com/questions/251781/how-to-find-the-kth-largest-element-in-an-unsorted-array-of-length-n-in-on/19089380
def QuickSelect(A, k):
    n = len(A)
    r = np.random.choice(n)
    pivot = A[r]
    A1 = []
    A2 = []
    # split into a pile A1 of small elements and A2 of big elements
    for i in range(n):
        if A[i] < pivot:
            A1.append(A[i])
        elif A[i] > pivot:
            A2.append(A[i])

    if k <= len(A1):
        # it's in the pile of small elements
        return QuickSelect(A1, k)
    elif k > (len(A) - len(A2)):
        # it's in the pile of big elements
        return QuickSelect(A2, k - (len(A) - len(A2)))
    else:
        # it's equal to the pivot
        return pivot


# ----------------------------------------------------------------------------------------------------------------------------
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
# https://www.youtube.com/watch?v=o1vuCrt7uYc

# This function returns k'th smallest element in arr[l..r] using QuickSort based method.
# ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT

def kthSmallest_by_QuickSort(arr, left, r, k):
    # If k is smaller than number of
    # elements in array
    if (k > 0) and (k <= r - left + 1):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        pos = partition(arr, left, r)

        # If position is same as k
        if pos - left == k - 1:
            return arr[pos]
        if pos - left > k - 1:  # If position is more,
            # recur for left sub array
            return kthSmallest_by_QuickSort(arr, left, pos - 1, k)

        # Else recur for right sub array
        return kthSmallest_by_QuickSort(arr, pos + 1, r, k - pos + left - 1)

    # If k is more than number of
    # elements in array
    return sys.maxsize


# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right
def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


# Driver Code
if __name__ == "__main__":
    # a = np.random.randint(low=0, high=30, size=8)
    array = [12, 3, 5, 7, 4, 1, 3, 19, 26]
    K = 3
    # print("K'th smallest element is", kthSmallest(arr, 0, n - 1, k))
    print("K'th smallest element is", QuickSelect(array, K))
