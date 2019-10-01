"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# https://leetcode.com/problems/two-sum/solution/
"""

def two_sum_me(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    bag = {}
    for i, num in enumerate(nums):
        n = target - num
        if n in bag:
            yield((bag[n], i))  # if we need values:  yield((num, n))
        else:
            bag[num] = i

arr = [1, 3, 4, 5, 0, 2]
sum_value = 7
print(list(two_sum_me(arr, sum_value)))
