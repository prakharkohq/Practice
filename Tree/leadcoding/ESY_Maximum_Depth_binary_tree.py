"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree.Node import TreeNode
class Solution:
    def maxDepth(self, root) -> int:
        def check(root):
            if root is None:
                return 0
            return 1 + max(check(root.left), check(root.right))

        return check(root)


if __name__ == "__main__":
    node = TreeNode(1)
    node.insert(2)
    node.insert(3)
    node.insert(4)
    node.insert(5)
    sol = Solution()
    print(sol.maxDepth(node))