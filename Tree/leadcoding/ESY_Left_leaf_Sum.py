"""
https://leetcode.com/problems/sum-of-left-leaves/

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

"""


## My Attempt
class Solution_1:
    def sumOfLeftLeaves(self, root) -> int:
        def find_sum(root, curr_sum):
            if root.left is None and root.right is None:
                curr_sum += root.val
                return curr_sum
            curr_sum += root.val
            find_sum(root.left, curr_sum)

        find_sum(root, 0)


class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        self.sum = 0

        # Base case
        def check_sum(root):
            if root:
                if root.left and root.left.left is None and root.right.right is None:
                    self.sum += root.left

                check_sum(root.left)
                check_sum(root.right)

        check_sum(root)
        return self.sum
