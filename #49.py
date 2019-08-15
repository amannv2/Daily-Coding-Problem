# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
#
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements
# 42, 14, -5, and 86.
#
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
#
# Do this in O(N) time.


def brute_force(array):
    max_sum = 0
    ultimate_sum = 0
    for i in range(len(array)):
        max_sum = 0
        for j in range(len(array)):
            if max_sum + array[j] > max_sum:
                max_sum += array[j]
        if max_sum > ultimate_sum:
            ultimate_sum = max_sum
    print(max_sum)


arr = [34, -50, 42, 14, -5, 86]

brute_force(arr)

# TODO:
# find sum -_-
