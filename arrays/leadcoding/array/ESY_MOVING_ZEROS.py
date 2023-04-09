"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

"""

# O(n^2) Time and O(1) space complexity First iteration
def solution(nums):
    saw_complete_array = False
    for index, item in enumerate(nums):
        # If element is zero
        if item == 0 and not saw_complete_array:
            zero = index
            # find next non zero
            for indx, non_zero in enumerate(nums[zero:]):
                if non_zero != 0:
                    nums[zero] = non_zero
                    nums[indx+zero] = 0
                    if indx+zero == len(nums) - 1:
                        saw_complete_array = True
                    break

    return nums


def moveZeroes(nums: list) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # wait while we find a non-zero element to
        # swap with you
        if nums[slow] != 0:
            slow += 1


"""
Best Solution 

We initialize two pointers i = 0, j = 0. Iterate j over range(len(nums)), and if nums[j] != 0, we swap nums[i] and 
nums[j], and increment i by 1. It is easy to see the loop invariant that nums[:i+1] contains all nonzero elements in
nums[:j+1] with relative order preserved. Hence when j reaches len(nums)-1, nums[:i+1] contains all nonzero elements
in nums with relative order preserved.

"""


def moveZeroes1(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums


if __name__ == "__main__":
    print(moveZeroes1([0,1,0,3,12]))