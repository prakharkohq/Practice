"""

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

Binary Search Problems
1. Search in Rotated Sorted Array
2. Find First and Last Position of Element in Sorted Array
3. Search a 2D Matrix
4. Find Peak Element
5. Find Smallest Letter Greater Than Target
6. Peak Index in a Mountain Array
7. Count of Range Sum
8. Search in Rotated Sorted Array II
9. Find Minimum in Rotated Sorted Array
10. Binary Search

"""


def find_min_in_sorted_rotated(nums):
    low, high = 0, len(nums) - 1
    while low < high:  # Kyoki yaha pr kahi bhi return nahi hai ek specific value ka to hame numbers ko hi shirnk karte
        # jaana hoga , if use lte this will loop infinitely
        mid = (low + high)//2
        if nums[mid] > nums[high]:
            # right half
            low = mid + 1
        else:
            high = mid

    return nums[low]


if __name__ == "__main__":
    nums = [5, 6, 7, 0, 1, 2, 4]
    print(find_min_in_sorted_rotated(nums))



## Solution if repeated values are present  --> Find Minimum in Rotated Sorted Array II

"""
    public int findMin(int[] nums) {
        
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mi = lo + (hi - lo) / 2;
            if (nums[mi] > nums[hi]) { 
                lo = mi + 1;
            }
            else if (nums[mi] < nums[lo]) { 
                hi = mi;
                lo++;
            }
            else { // nums[lo] <= nums[mi] <= nums[hi] 
                hi--;
            }
        }
        
        return nums[lo];
    }
"""

# Explanation

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set left and right bounds
        left, right = 0, len(nums) - 1

        # left and right both converge to the minimum index;
        # DO NOT use left <= right because that would loop forever
        while left < right:
            # find the middle value between the left and right bounds (their average);
            # can equivalently do: mid = left + (right - left) // 2,
            # if we are concerned left + right would cause overflow (which would occur
            # if we are searching a massive array using a language like Java or C that has
            # fixed size integer types)
            mid = (left + right) // 2

            # the main idea for our checks is to converge the left and right bounds on the start
            # of the pivot, and never disqualify the index for a possible minimum value.

            # in normal binary search, we have a target to match exactly,
            # and would have a specific branch for if nums[mid] == target.
            # we do not have a specific target here, so we just have simple if/else.

            if nums[mid] > nums[right]:
                # we KNOW the pivot must be to the right of the middle:
                # if nums[mid] > nums[right], we KNOW that the
                # pivot/minimum value must have occurred somewhere to the right
                # of mid, which is why the values wrapped around and became smaller.

                # example:  [3,4,5,6,7,8,9,1,2]
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] > nums[right], we know that at some point to the right of mid,
                # the pivot must have occurred, which is why the values wrapped around
                # so that nums[right] is less then nums[mid]

                # we know that the number at mid is greater than at least
                # one number to the right, so we can use mid + 1 and
                # never consider mid again; we know there is at least
                # one value smaller than it on the right
                left = mid + 1

            else:
                # here, nums[mid] <= nums[right]:
                # we KNOW the pivot must be at mid or to the left of mid:
                # if nums[mid] <= nums[right], we KNOW that the pivot was not encountered
                # to the right of middle, because that means the values would wrap around
                # and become smaller (which is caught in the above if statement).
                # this leaves the possible pivot point to be at index <= mid.

                # example: [8,9,1,2,3,4,5,6,7]
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] <= nums[right], we know the numbers continued increasing to
                # the right of mid, so they never reached the pivot and wrapped around.
                # therefore, we know the pivot must be at index <= mid.

                # we know that nums[mid] <= nums[right].
                # therefore, we know it is possible for the mid index to store a smaller
                # value than at least one other index in the list (at right), so we do
                # not discard it by doing right = mid - 1. it still might have the minimum value.
                right = mid

        # at this point, left and right converge to a single index (for minimum value) since
        # our if/else forces the bounds of left/right to shrink each iteration:

        # when left bound increases, it does not disqualify a value
        # that could be smaller than something else (we know nums[mid] > nums[right],
        # so nums[right] wins and we ignore mid and everything to the left of mid).

        # when right bound decreases, it also does not disqualify a
        # value that could be smaller than something else (we know nums[mid] <= nums[right],
        # so nums[mid] wins and we keep it for now).

        # so we shrink the left/right bounds to one value,
        # without ever disqualifying a possible minimum
        return nums[left]

# Binary Search Concept


def binary_search_my_attempt(nums, low, high, key):
    """
    Problems in my recursive functions are
    1 : I have not defined any base case for my given function so this program iterates indefinetley resulting in TLE except
    2 : Arrays are not forwarded in next stage of recursive calls Like mid is not adjusted for next call
    """

    mid = int((low + high) / 2)
    if key == nums[mid]:
        return mid
    if key > nums[mid]:
        return binary_search_my_attempt(nums, mid, high, key)
    elif key < nums[mid]:
        return binary_search_my_attempt(nums, low, mid, key)

    return -1


def binary_search(nums, low, high, target):
    if low <= high:
        mid = int((low + high) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binary_search(nums, low, mid - 1, target)
        else:
            return binary_search(nums, mid + 1, high, target)
    else:
        return -1


def binary_search_caller(nums, target):
    low = 0
    high = len(nums) - 1
    index = binary_search(nums, low, high, target)
    return index
