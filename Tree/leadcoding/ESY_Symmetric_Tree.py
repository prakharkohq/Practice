"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Tree.Node import TreeNode

"""
Finding the symmetric tree should be a problem where we compare left.left tree to right.right 
and right.left with left.right 
We need to keep on doing this process so repeated part could be extracted as a function 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Function to do the operations
        def check(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            if left.val == right.val:
                return check(left.left, right.right) and check(left.right, right.left)
            else:
                return False

        if root is None:
            return True
        else:
            return check(root.left, root.right)