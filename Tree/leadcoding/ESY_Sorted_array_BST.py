"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:


Concept here is as the numbers are sorted always root will be the middle element in the list of numbers

asymptotic complexity is bad. Slices take O(s) where 's' is the size of the slice.
Therefore this algorithm has runtime O(n lg n), space O(n), wheras it could be done in
O(n) runtime and O(lg n) space complexity
"""
from Tree.Node import TreeNode


## Without using slices

def sortedArrayToBST(nums):
    def check(low, high):
        # Base condition
        if low > high:
            return None

        mid = (low + high) // 2
        root = TreeNode(nums[mid])
        root.left = check(low, mid - 1)
        root.right = check(mid + 1, high)
        return root

    return check(0, len(nums) - 1)
