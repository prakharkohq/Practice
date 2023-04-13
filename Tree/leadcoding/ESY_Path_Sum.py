"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.

A leaf is a node with no children.
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
"""


# My attempt
class Solution_1:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def check_root_sum(root, curr_sum, target_sum):
            if root.left is None and root.right is None:
                # leaf node hai ye
                if curr_sum == target_sum:
                    return True
                return False
            curr_sum += root.val
            return check_root_sum(root.left, curr_sum, target_sum) or check_root_sum(root.right, curr_sum, target_sum)

        return check_root_sum(root, 0, targetSum)


"""
Improvements on my attempt
O(N) Solution we can reuse the target sum variable present
"""

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False

        # check for a leaf node and find out value is equal to sum which is a terminal condition

        if root.left is None and root.right is None and root.val == targetSum:
            return True

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)