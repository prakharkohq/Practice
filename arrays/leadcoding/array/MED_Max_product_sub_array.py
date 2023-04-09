"""
Given an integer array nums, find a  subarray that has the largest product, and return the product.
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

"""
This solution will fail for cases like this : [-2,3,-4] Your output would be 3 Expected output would be 24
this is optimisation on previous kedane's algorithm
"""


def solution(nums):
    max_multiple_so_far, max_multiple_here = nums[0], nums[0]
    for i in range(1, len(nums)):
        max_multiple_here = max(max_multiple_here*nums[i], nums[i])
        max_multiple_so_far = max(max_multiple_so_far, max_multiple_here)
    return max_multiple_so_far


def solution_my_attempt(nums):
    global_max, prev_min, prev_max = nums[0], nums[0], nums[0]
    for num in nums[1:]:
        # Here we need to get current value of max and min to compare against previous max and min
        # yaha teen number is lie liye gaye hai kyoki jo previous number mein sabse chota hai wo bhi max result possible
        curr_max = max(prev_max*num, prev_min*num , num)
        curr_min = min(prev_max*num, prev_min*num , num)
        global_max = max(curr_max, global_max)
        prev_max = curr_max
        prev_min = curr_min

    return global_max

def maxProduct(nums):
    ## TIME COMPLEXITY : O(N) ##
    ## SPACE COMPLEXITY : O(1) ##

    # 1. Edge Case : Negative * Negative = Positive
    # 2. So we need to keep track of minimum values also, as they can yield maximum values.

    global_max = prev_max = prev_min = nums[0]
    for num in nums[1:]:
        curr_min = min(prev_max * num, prev_min * num, num)
        curr_max = max(prev_max * num, prev_min * num, num)
        global_max = max(global_max, curr_max)
        prev_max = curr_max
        prev_min = curr_min
    return global_max


if __name__ == "__main__":
    print(maxProduct([-2,0,-1]))