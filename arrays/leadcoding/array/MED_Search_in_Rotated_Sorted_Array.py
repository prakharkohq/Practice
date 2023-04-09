"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

"""
"""
Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

If target is let's say 7, then we adjust nums to this:
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

And then we can simply do ordinary binary search.

Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at. 
And the adjustment is done by comparing both the target and the actual element against nums[0].

If nums[mid] and target are "on the same side" of nums[0], we just take nums[mid]. 
Otherwise we use -infinity or +infinity as needed.
"""


def search_my_attempt(nums, target):
    low, high = 0, len(nums) -1
    # Finding the right place for the binary search
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]: #pehla step hai sorted array findout karne ki koshish karo kaha pr array sorted hai jisme target ko use karne ka koi sense nahi hai
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else: # first left half is not sorted and according to the plan try to find the right place on second right half for target
            if nums[mid] < target <= nums[high]:
                low = mid+1
            else:
                high = mid - 1
    return -1


def search(nums, target):
    #   1. have to find rotation point
    #   2. make mid = pivot element, start and end
    #   3. IMP : If Pivot element is larger than the first element in the array,
    #       i.e. the part of array from the first element to the pivot one is non-rotated.
    #   4. If the target is in that non-rotated part as well: go left: otherwise go right.
    #   5. Pivot element is smaller than the first element of the array, i.e. the rotation index is
    #       somewhere between 0 and mid. That means that the part of array from the pivot element to
    #       the last one is non-rotated.
    #   6. If target is in that non-rotated part as well: go right: else left.

    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]: return mid
        if nums[mid] >= nums[start]:  # indicates non-rotated array
            # target < nums[mid] and target >= nums[start]
            if nums[mid] > target >= nums[start]:  # check for target in non-rotated part
                end = mid - 1
            else:
                # start ko second half pr lekar jaao
                start = mid + 1
        else:  # indicates rotated array
            # target <= nums[end] and target > nums[mid]
            if nums[end] >= target > nums[mid]:  # check for target in non-rotated part
                start = mid + 1
            else:
                end = mid - 1
    return -1

# Problems with my approach is

"""
Using  recursion No Invalidation of invalid entries while looping 
Concept was right
"""


def solution_my_attempt(nums, low, high, target):
    if low < high:
        mid = (low+high) // 2
        if nums[mid] == target:
            return mid
        elif nums[low] <= target < nums[mid]:
            return solution_my_attempt(nums, low, mid-1, target)
        else:
            return solution_my_attempt(nums, mid+1, high, target)
    else:
        return -1


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 2
    print(search_my_attempt(nums, target))