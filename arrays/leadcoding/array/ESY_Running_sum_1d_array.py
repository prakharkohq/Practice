
"""
Running Sum of 1d Array  Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

"""

# O(n) space O(n) time solution
from itertools import accumulate


def solution(nums):
    curr_sum = 0
    response_arr = []
    if len(nums) == 1:
        return nums
    for item in nums:
        curr_sum += item
        response_arr.append(curr_sum)

    return response_arr


# O(1) Space O(n) time and also it is inplace conversion not a very healthy practice
def solution_const(nums):
    curr_sum = 0
    if len(nums) == 1:
        return nums
    for index, item in enumerate(nums):
        curr_sum += item
        nums[index] = curr_sum

    return nums


def runningSum(nums):
    from itertools import accumulate
    return accumulate(nums)


if __name__ == "__main__":
    ans = runningSum([1,2,3,4,5])
    for item in ans:
        print(item)